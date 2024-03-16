# Import
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

# Form results
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # ottenere l'immagine selezionata
        selected_image = request.form.get('image-selector')
        # Consegna #2. Ricevere il testo
        text_top  = request.form.get('textTop')
        text_botton = request.form.get('textBottom')
        # Consegna #3. Ricezione del posizionamento del testo
        text_y_top = request.form.get('textTop_y')
        text_y_botton = request.form.get('textBotto,_y')       
        # Consegna #3. Ricezione del colore del testo
        color_select = request.form.get('color-selector')

        return render_template('index.html', 
                               # Visualizzazione dell'immagine selezionata
                               selected_image=selected_image, 
                               # Consegna #2. Visualizzazione del testo
                                ttop=text_top,
                                tbottom=text_botton,
                               # Consegna #3. Visualizzazione del posizionamento del testo
                                ytop=text_y_top,
                                ybotton=text_y_botton,
                               # Consegna #3. Visualizzazione del colore 
                                c=color_select

                               )
    else:
        # Visualizzazione predefinita della prima immagine
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
