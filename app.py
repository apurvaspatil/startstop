import webbrowser
from flask import Flask , request
import os

app= Flask(__name__)

@app.route('/')
def index():
    return '<html> start stop </html>'


@app.route('/start', methods=['GET'])
def start_browser():
    browser_name= request.args.get("browser")
    url= request.args.get("url")
    if browser_name=='chrome':
        webbrowser.register('chrome',
        None,
        webbrowser.BackgroundBrowser("C://Program Files (x86)/Google/Chrome/Application/chrome.exe"))
        webbrowser.get('chrome').open(url)
        return '<html> chrome succesfully opened</html>'
    elif browser_name == 'firefox':
        webbrowser.register('firefox',
        None,
        webbrowser.BackgroundBrowser("C://Program Files/Mozilla Firefox/firefox.exe"))
        webbrowser.get('firefox').open(url)
        return '<html> firefox succesfully opened</html>'
    else:
        return '<html> browser not found </html>'

@app.route('/stop', methods=['GET'])
def stop_browser():
    browser_name = request.args.get("browser")
    if browser_name == 'chrome':
        os.system("taskkill /im chrome.exe /f")
        return '<html> Chrome stopped</html>'
    elif browser_name =='firefox':
        os.system("taskkill /im firefox.exe /f")
        return '<html> firefox stopped </html>'
    else:
        return '<html> browser notfound </html>'    


'''@app.route('/geturl' methods=['PUT'])
def cleanup_browser():
    browser_name = request.args.get("browser")
    if browser_name == 'chrome':'''
        
        
           
    
if __name__ == "__main__":
    app.run()