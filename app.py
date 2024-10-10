from flask import Flask, render_template, request
import json

app  = Flask(__name__)

app.static_folder = 'static'
@app.route("/", methods=["GET"])

def ceaser_cipher_decrypt():
    if request.method == "GET":
        if(request.args.get("cipher") == None):
            return render_template("./index.html")
        elif(request.args.get('cipher') == ''):
            return "<html><body> <h1>Invalid Text</h1></body></html>"
        else:
            input_text = request.args.get("cipher")
            cipher_text = str(input_text)
            alpha_array = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            output_answers = []
            output_formatted_string = []

            for t in range(25):
                empty_string = ""
                cipher_string = str(cipher_text)
                for n in cipher_string:
                    if n == " " or n == "_":
                        empty_string = empty_string + str(n)
                    else:
                        n = n.upper()
                        current_index = alpha_array.index(n)
                        new_index_calculation = int((current_index - t) % 26)
                        decrypted_word = alpha_array[new_index_calculation]
                        empty_string = empty_string + str(decrypted_word)



                output_answers.append(empty_string)
                
            return render_template("./decryptedList.html", decrypted_text = output_answers)
        

# if(__name__ == "__main__"):
#     app.run(debug=True)
