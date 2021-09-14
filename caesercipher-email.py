import smtplib
import re


def get_domain(email):
    match = re.search('@', email)
    n = match.start()

    match2 = re.search('.com', email)
    m = match2.start()

    s = email[n + 1:m]
    return s


def encrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            # Encrypt uppercase characters
            if (char.isupper()):
                result += chr((ord(char) + s - 65) % 26 + 65)

            # Encrypt lowercase characters
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char

    return result


def send_mails(message):
    global smtp_obj, email
    print("Please use APP PASSWORD if using GMAIL ")
    print()
    print()

    while (True):
        try:
            email = input("Email ID :")
            password = input("Password : ")
            print()
            print("Please wait while we establish a secure connection.....")
            print("\n")
            s = get_domain(email)
            smtp_obj = smtplib.SMTP('smtp.' + s + '.com', 587)
            smtp_obj.ehlo()
            smtp_obj.starttls()
            smtp_obj.login(email, password)

        except:
            print("Some error occurred.Please re-enter your email and password.")
            continue

        else:
            print("Connected to your mail server.")
            break
    print()
    print()

    subject = input("SUBJECT : ")
    print()

    msg = 'Subject: ' + subject + '\n' + message

    try:
        email_to_send = input('To : ')

        print('\nSending Email....')
        smtp_obj.sendmail(email, email_to_send, msg)

    except:
        print("Some error occurred. ")

    else:

        smtp_obj.quit()

        print()
        print("Email sent. ")


def get_input():
    msg = input("Message to be encrypted and sent : ")
    print('\n')
    s = int(input('Shift = '))
    msg += ('shift = ' + str(s))
    enc_msg = encrypt(msg, s)

    send_mails(enc_msg)


def main():
    get_input()


if __name__ == '__main__':
    main()
