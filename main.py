import webapp2
from caesar import encrypt
import cgi

encrypt_form = """
<!DOCTYPE html>
<html>
    <head>
        <title>Caesar</title>
    </head>
    <body>
        <form method="post">
            <label>
            Text to encrypt:
                <input type="text" name="text">
            </label>
            <br>
            <label>
            Rotation amount:
                <input type="number" name="rot">
            </label>
            <br>
            <input type="submit" value="Encrypt">
        </form>
    </body>
</html>
"""

class CaesarEncryption(webapp2.RequestHandler):
    def get(self):
        self.response.write(encrypt_form)

    def post(self):

        text = cgi.escape(self.request.get("text"), quote = True)
        rot = cgi.escape(self.request.get("rot"), quote = True)
        answer = encrypt(text, int(rot))
        self.response.write(answer)

app = webapp2.WSGIApplication([
    ('/', CaesarEncryption)
], debug=True)
