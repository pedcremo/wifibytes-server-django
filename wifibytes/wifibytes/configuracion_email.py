# encoding:utf-8
import smtplib
from email.utils import formataddr
from smtplib import SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from datos_empresa.models import DatosEmpresa


class Email:

    # el email donde AltreBit Recive los correos
    #EMAIL = 'info@wifibytes.com'

    def __init__(self, *args, **kwargs):
        ########### EMAIL CONF ############
        company = DatosEmpresa.objects.filter(datos_empresa_default=True).first()
        email_conf = company.configuracion_email

        # A nombre de quien se envian los emails
        self.EMAIL = email_conf.email_receiver
        self.NAME_EMAIL = email_conf.emailname_receiver
        # Quien Envia
        self.USER = email_conf.email_sender
        self.PASSWORD = email_conf.email_sender_password
        self.SERVER = email_conf.server
        self.PORT = email_conf.port

    # Email interno para informar de la creacion de una causa
    def sendemail_causa(self, remitente, nombre):

        subject = 'Nueva causa'
        body = remitente.encode(
            'utf8') + ' ha creado la causa ' + nombre.encode('utf8')
        ret = Email.sendemail(self, self.EMAIL, body, subject)
        return ret

    # Email para informar al usuario de la creacion de una causa
    def sendemail_gracias(self, email, remitente, nombre):
        try:
            company = DatosEmpresa.objects.filter(datos_empresa_default=True).first()
            name = str(company.name)
        except Exception as error:
            name = '[EMPRESA]'

        subject = name + ' te da las gracias por crear una causa'
        body = 'Muchas gracias ' + \
            remitente.encode('utf8') + ' por crear la causa ' + \
            nombre.encode('utf8') + ' la tendremos en cuenta.'
        ret = Email.sendemail(self, email, body, subject)
        return ret

    def sendemail_updatepass(self, newpass, email, codcliente):
        try:
            company = DatosEmpresa.objects.filter(datos_empresa_default=True).first()
            name = str(company.name)
        except Exception as error:
            name = '[EMPRESA]'

        subject = name + ' contraseña actualizada'
        body = 'Muchas gracias por confiar en ' + name + ' aqui tienes tus datos: ' + \
            '\n Cod. Cliente: ' + str(codcliente) + \
            '\n Nueva contraseña: ' + str(newpass)
        ret = Email.sendemail(self, email, body, subject)
        return ret

    def sendemail_contacto(self, nombre, telefono, email, descripcion):

        subject = 'Nuevo contacto'
        body = '"' + descripcion.encode('utf8') + '"' + '\n \n' + '\n' + 'Nombre: ' + nombre.encode(
            'utf8') + '\n' + 'Email: ' + email.encode('utf8') + '\n' + 'Telefono: ' + telefono.encode('utf8')
        ret = Email.sendemail(self, self.EMAIL, body, subject)
        return ret

    def sendemail(self, email, body, subject, template=False):
        #READ https://docs.aws.amazon.com/ses/latest/DeveloperGuide/examples-send-using-smtp.html python example
        #how to use AWS simple email service to send emails
        # Quien recive
        RECEIVERS = email
        SUBJECT = subject
        TEXT = body
        ###################################

        msg = MIMEMultipart()
        #HARD FIX
        #msg['From'] = self.USER
        msg['From'] = formataddr((self.NAME_EMAIL, self.EMAIL))
        #msg['From'] = self.EMAIL
        msg['To'] = RECEIVERS
        msg['Subject'] = SUBJECT

        if template:
            # pynliner se utiliza para eliminar el tag style y añadir el css
            # en la misma linia para que se mantenga el estilo en gmail y en
            # otros servicios que eliminan el tag 'style'
            msg.attach(MIMEText(TEXT, 'html'))
            # msg.attach(MIMEText(TEXT, 'html'))
        else:
            msg.attach(MIMEText(TEXT))

        try:
            print("server:%s port:%s",self.SERVER,self.PORT)
            smtpObj = smtplib.SMTP(self.SERVER, self.PORT)
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.ehlo()
            print("credentials user:%s password:%s",self.USER,self.PASSWORD)
            smtpObj.login(self.USER, self.PASSWORD)
            #HARD BAD 
            #smtpObj.sendmail(self.USER, RECEIVERS, msg.as_string())
            smtpObj.sendmail(self.EMAIL, RECEIVERS, msg.as_string())
            smtpObj.quit()
            print("Successfully sent email")
            return True
        except SMTPException as e:
            print("Error: unable to send email")
            print(str(e))
