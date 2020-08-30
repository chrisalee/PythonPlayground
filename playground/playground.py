from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    
@app.route('/')                           
def playground():
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template("index.html")

@app.route('/play')   # should i be doing these in different html things for each new page display??
def box1(x):
    print('*'*40)
    return render_template("index.html", box1=(box1))

@app.route('/play/<number>')   #  let the user pick the number of boxes
def level2(number):
    return render_template("index.html", number=int(number) )

#  have not figured out the color yet    @app.route('/play/<number>/<color>) #  let the user pick the number of boxes and the color
#  have not figured out the color yet    def level3(number, color):
#  have not figured out the color yet        return render_template("index.html", number=int(number), color=background("color"))

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.