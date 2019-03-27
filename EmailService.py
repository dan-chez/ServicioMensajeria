import smtplib
import base64

email_user = 'correo@email.com'
email_password = 'password2019'

class ServicioEmail():

    def decoBase64UrlSafe(self,s):
        var=base64.urlsafe_b64decode(s + '=' * (4 - len(s) % 4))
        return str(var, 'utf-8')
#Las variables que llegan a la funcion sendEmail vienen codificadas en base64 URL Safe
    def sendEmail(self,nombreGrupo,namefrom,emailto,subject,body):

        newnamefrom = self.decoBase64UrlSafe(namefrom)
        newemailto = self.decoBase64UrlSafe(emailto)
        newsubject = self.decoBase64UrlSafe(subject)
        newbody = self.decoBase64UrlSafe(body)
        newnombreGrupo = self.decoBase64UrlSafe(nombreGrupo)


        
        message = """From: %s <%s>
To: %s <%s>
MIME-Version: 1.0
Content-type: text/html
Subject: %s

%s
        """ % (newnamefrom, email_user, newnombreGrupo, newemailto.split(), newsubject, newbody)

        try:
            server = smtplib.SMTP_SSL('servidor_email', 465)
            server.ehlo()
            server.login(email_user, email_password)
            server.sendmail(email_user, newemailto.split(), message)
            server.close()
            return "OK"
            #server.starttls()
        except:
            return "BAD"

    #%(sent_from, ", ".join(to), subject, body)  Para enviar a varios correos


        
        


