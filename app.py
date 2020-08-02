from flask import Flask, render_template,request    
app = Flask(__name__, template_folder='template')


@app.route('/')
def home():
    q=request.args.get('qry')
    if q=='name':
        return render_template('reply.html', content='Akash')
    elif q=='city':
        return render_template('reply.html', content='Kakinada')
    elif q=='dad':
        return render_template('reply.html', content=myfunc())
    else: 
        return render_template('index.html')
        
   
def myfunc():
    a= 'PSR'
    b=' Kumar'
    return a+b


if __name__ == '__main__':
    app.run()