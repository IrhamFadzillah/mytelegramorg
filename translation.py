class Translation(object):
    START_TEXT = """Hi !
Mau nyari API ID sama HASH kah? 😬
Masukan nomer telpon anda dengan menggunakan +62

/start at any stage to re-enter your details"""
    AFTER_RECVD_CODE_TEXT = """Done
Kirim kesini kode yang telah dikirim oleh pihak telegramnya!

kode ini hanya digunakan untuk tujuan mendapatkan ID APP dari my.telegram.org


/start at any stage to re-enter your details"""
    BEFORE_SUCC_LOGIN = "recieved code. Scarpping web page ..."
    ERRED_PAGE = "something wrongings. failed to get app id. \n\n@ManusiaRakitan"
    CANCELLED_MESG = "Bye! Please re /start the bot conversation"
    IN_VALID_CODE_PVDED = "sorry, but the input does not seem to be a valid Telegram Web-Login code"
    IN_VALID_PHNO_PVDED = "sorry, but the input does not seem to be a valid phone number"
