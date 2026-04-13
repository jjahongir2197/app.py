from flask import Flask, render_template

app = Flask(__name__)

@app.route("/names")
def names():

    names = [

        "Jahongir",
        "Ali",
        "Vali",
        "Muhammad",
        "Azizbek",
        "Sardor",
        "Bekzod"

    ]

    longest = max(names, key=len)
    shortest = min(names, key=len)

    lengths = []

    for n in names:

        lengths.append({

            "name": n,

            "length": len(n)

        })

    return render_template(
        "names.html",
        lengths=lengths,
        longest=longest,
        shortest=shortest
    )


if __name__ == "__main__":
    app.run(debug=True)
