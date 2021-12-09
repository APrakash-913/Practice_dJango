# I have created this file-AP    

## Hmm log ko ek Attribute Error bhi milega i.e.
from django.http import HttpResponse
from django.shortcuts import render



def index(request): 
    # Agar request set ni karenge tb, website pe hmme typeError milega.
    # Update karne ka tension ni lena hai, dJango apne aap sb kuch update karte rahata hai.
    return HttpResponse('''<h1>hello AP</h1> <a href= "https://ticker.finology.in/company/SAFARI">1. Stocks </a>
                        <a href= "https://github.com/">2. GitHub </a>
                        <a href= "https://www.youtube.com/">3. YouTube </a>
                        <a href= "https://www.flipkart.com/">4. Flipkart </a>
                        <a href= "https://www.amazon.com/">5. Amazon </a>  ''')

def about(request): 
    return HttpResponse("About AP")
#--------------------------------------------PRACTICE PURPOSE ONLY(JUST IGNORE)-------------------------------------------------------------------------------#
                                      
def index1(request):
    #return HttpResponse("HOME")
    return render(request,"index1.html")

def removepunc(request):
    # Get the text
    djtext=print(request.POST.get('text', 'default')) #--> ye HTML me textarea me jo "name" ka value hai usko print karega else "default" ko print karega.
    print(djtext)
    # Analyse the text
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse('''<h2>Capitalize first</h2> <a href="http://127.0.0.1:8000">back to home</a>''')

def newlineremove(request):
    return HttpResponse('''<h2>new line remover</h2> <a href="http://127.0.0.1:8000">back to home</a>''')      

def charremove(request):
    return HttpResponse('''<h2>character remover</h2> <a href="http://127.0.0.1:8000">back to home</a>''')      

def spaceremove(request):
    return HttpResponse('''<h2>space remover</h2> <a href="http://127.0.0.1:8000">back to home</a>''')


##----------------------------------------------------MAIN BODY---------------------------------------------------## 

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default') #--> ye HTML me textarea me jo "name" ka value hai usko print karega else "default" ko print karega.
                # 'GET' ka data handle karne ka ek limitation hota hai, so, we use POST.
    print(djtext)

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount=request.POST.get('charcount','off')
    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        print(params)
        # Analyze the text
        return render(request, 'analyze.html', params)
    
    elif (charcount=='on'):
        params={'purpose':'Character Count','analyzed_text':len(djtext)}
        return render(request,'analyze.html',params)   

    else:
        return HttpResponse("Error")        