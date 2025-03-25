from groq import Groq

from flask import Flask, render_template, request
app = Flask(__name__)
from datetime import datetime

AI_KEY = "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"

client = Groq(api_key = AI_KEY)
def ai_call(tahun_lahir):
    try:
        chat_completion = client.chat.completions.create(
            messages= [
                    {
                    "role": "user",
                    "content": f"Berikan saya satu fakta teknologi menarik dan paling terkenal di tahun {tahun_lahir}"
                }
            ],
            model = "llama-3.2-3b-preview",
            stream = False
        )
        
        ai_output = chat_completion.choices[0].message.content
        ai_output = ai_output.replace("**", "")
        return ai_output
    
    except Exception:
        return "Maaf fitur AI saat ini tidak bisa digunakan"
@app.route("/")
def index():
    web_title = 'halaman utama'
    return render_template('index.html', data = web_title)

@app.route("/about")
def about():
    web_title = 'halaman about'
    return render_template('about.html', data = web_title)

@app.route("/usia", methods=['GET', 'POST'])
def cek_usia():
    if request.method == 'POST':
        tahun_lahir = int(request.form['tahun_lahir'])
        tahun_sekarang = datetime.now().year
        usia = tahun_sekarang - tahun_lahir
        
        # Program AI Groq 
        ai_output = ai_call(tahun_lahir)
        # print(ai_output)
        
        return render_template('cek_usia.html', usia = usia, tahun_lahir = tahun_lahir, ai_output = ai_output)
        
    return render_template('cek_usia.html', usia = None)

if __name__ == "__main__":
    app.run(debug=True)
