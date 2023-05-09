import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

noticeURL = "https://iiitn.ac.in/news.php"
feesURL = "https://iiitn.ac.in//page.php?name=fees&id=42"
calendarURL = "https://iiitn.ac.in//page.php?name=academic-calendar&id=257"

@app.route('/acadmic-calendar',methods=['GET'])
def getCalander():
    try:
        req = requests.get(calendarURL)
        lis = []
        soup = BeautifulSoup(req.content,'html.parser')
        container = soup.find('div',class_ = "panel-body")

        for ele in container.find_all('tbody'):
            for td in ele.find_all('td'):
                strong = td.find('strong')
                if strong:
                    atag = strong.find('a')
                    if atag:
                        link = atag['href']
                        lis.append(link)
        return jsonify(lis)
    except:
        return "Can't reach the server right now"

@app.route('/fees', methods=['GET'])
def getFees():
    try:
        req = requests.get(feesURL)

        soup = BeautifulSoup(req.content, 'html.parser')
        container = soup.find('div', class_="blog-slide")

        lis = []

        for ele in container.find_all('p'):
            strong = ele.find('strong')
            if strong:
                txt = strong.text
                atag = strong.find('a')
                if atag:
                    if txt == "1st Year Academic Fees Details 2020-2021 Click Here  ":
                        txt = txt.rsplit(' ', 3)[0]
                    else:
                        txt = txt.rsplit(' ', 2)[0]
                    link = atag['href']
                    lis.append({
                        "text": txt,
                        "link": link
                    })
                else:
                    lis.append({
                        "heading": txt,
                    })

        aTaginli = container.find('li').find('a')
        lis.append({
            "text": aTaginli.text,
            "link": aTaginli['href']
        })

        return jsonify(lis)
    except:
        return "Can't reach 'https://iiitn.ac.in//page.php?name=fees&id=42' at the moment"


@app.route('/faculty-notices', methods=['GET'])
def getFacultyNotices():
    try:
        req = requests.get(noticeURL)

        soup = BeautifulSoup(req.content, 'html.parser')
        elements = soup.find(id="div_FacultyNotices").find_all('a')
        lis = []

        for e in elements:
            title = e.string
            link = e['href']
            lis.append({
                "title": title,
                "link": link,
            })

        return jsonify(lis)
    except:
        return "Can't reach 'https://iiitn.ac.in/news.php' at the moment"


@app.route('/student-notices', methods=['GET'])
def getStudentNotices():
    try:
        req = requests.get(noticeURL)

        soup = BeautifulSoup(req.content, 'html.parser')
        elements = soup.find(id="div_StudentNotices").find_all('a')
        lis = []

        for e in elements:
            title = e.string
            link = e['href']
            lis.append({
                "title": title,
                "link": link,
            })

        return jsonify(lis)
    except:
        return "Can't reach 'https://iiitn.ac.in/news.php' at the moment"


@app.route('/faculty-achievements', methods=['GET'])
def getFacultyAchievements():
    try:
        req = requests.get(noticeURL)

        soup = BeautifulSoup(req.content, 'html.parser')
        elements = soup.find(id="div_FacultyAchievement").find_all('a')
        lis = []

        for e in elements:
            title = e.string
            link = e['href']
            lis.append({
                "title": title,
                "link": link,
            })

        return jsonify(lis)
    except:
        return "Can't reach 'https://iiitn.ac.in/news.php' at the moment"


@app.route('/student-achievements', methods=['GET'])
def getStudentAchievements():
    try:
        req = requests.get(noticeURL)

        soup = BeautifulSoup(req.content, 'html.parser')
        elements = soup.find(id="div_StudentAchievement").find_all('a')
        lis = []

        for e in elements:
            title = e.string
            link = e['href']
            lis.append({
                "title": title,
                "link": link,
            })

        return jsonify(lis)
    except:
        return "Can't reach 'https://iiitn.ac.in/news.php' at the moment"


@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
