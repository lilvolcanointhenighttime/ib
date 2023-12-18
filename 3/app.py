from encryption import generate_private_key, generate_public_key_pem, load_public_key_pem, encrypt_message, decrypt_message

def KSumm(text, MaxVal, public_key):
    text_list = list(text)
    accum = 0
    for value in text_list:
        accum += ord(value)
    if accum > MaxVal:
        accum = accum % MaxVal
        return encrypt_message(str(accum).encode(), public_key)
    return encrypt_message(str(accum).encode(), public_key)

def SummKodBukvOtkr(text, a, b, c, t0, public_key):
    p = len(text)
    text_list = list(text)
    
    X = []
    for value in (text_list):
        value_binary = bin(ord(value))[2:]
        while len(value_binary) < 8:
            value_binary = '0' + value_binary
        X.append(value_binary)

    T = []
    t_current = t0
    for _ in range(0, p):
        t_current_binary = bin(t_current)[2:]
        while len(value_binary) < 8:
            value_binary = '0' + value_binary
        T.append(t_current_binary)
        t_current = (a*t_current + b) % c

    Y = [int(X[i], 2) ^ int(T[i], 2) for i in range(len(T))]
    return encrypt_message(str(sum(Y) % c).encode(), public_key)

def main():
    # Генерация приватного и бубличного ключа
    private_key = generate_private_key()
    public_key = generate_public_key_pem(private_key)
    loaded_public_key = load_public_key_pem(public_key)

    # Условие согласно варианту 4
    a = 19
    b = 3
    c = 256
    MaxVal = 255
    t0 = 101

    # Нахождение контрольной суммы для всех P согласно варианту 4
    Pa = '02468'
    Pa_KSumm = KSumm(Pa, MaxVal, loaded_public_key)
    decoded_Pa_KSumm = decrypt_message(Pa_KSumm, private_key).decode()
    Pa_SummKodBukvOtkr = SummKodBukvOtkr(Pa, a, b, c, t0, loaded_public_key)
    decoded_Pa_SummKodBukvOtkr = decrypt_message(Pa_SummKodBukvOtkr, private_key).decode()
    # print(Pa_KSumm)
    # print(Pa_SummKodBukvOtkr)
    print(decoded_Pa_KSumm)
    print(decoded_Pa_SummKodBukvOtkr)

    Pb = '86420'
    Pb_KSumm = KSumm(Pb, MaxVal, loaded_public_key)
    decoded_Pb_KSumm = decrypt_message(Pb_KSumm, private_key).decode()
    Pb_SummKodBukvOtkr = SummKodBukvOtkr(Pb, a, b, c, t0, loaded_public_key)
    decoded_Pb_SummKodBukvOtkr = decrypt_message(Pb_SummKodBukvOtkr, private_key).decode()
    # print(Pb_KSumm)
    # print(Pb_SummKodBukvOtkr)
    print(decoded_Pb_KSumm)
    print(decoded_Pb_SummKodBukvOtkr)

    Pv = '1000009'
    Pv_KSumm = KSumm(Pv, MaxVal, loaded_public_key)
    decoded_Pv_KSumm = decrypt_message(Pv_KSumm, private_key).decode()
    Pv_SummKodBukvOtkr = SummKodBukvOtkr(Pv, a, b, c, t0, loaded_public_key)
    decoded_Pv_SummKodBukvOtkr = decrypt_message(Pv_SummKodBukvOtkr, private_key).decode()
    # print(Pv_KSumm)
    # print(Pv_SummKodBukvOtkr)
    print(decoded_Pv_KSumm)
    print(decoded_Pv_SummKodBukvOtkr)

    Pg = '1900000'
    Pg_KSumm = KSumm(Pg, MaxVal, loaded_public_key)
    decoded_Pg_KSumm = decrypt_message(Pg_KSumm, private_key).decode()
    Pg_SummKodBukvOtkr = SummKodBukvOtkr(Pg, a, b, c, t0, loaded_public_key)
    decoded_Pg_SummKodBukvOtkr = decrypt_message(Pg_SummKodBukvOtkr, private_key).decode()
    # print(Pg_KSumm)
    # print(Pg_SummKodBukvOtkr)
    print(decoded_Pg_KSumm)
    print(decoded_Pg_SummKodBukvOtkr)

if __name__ == '__main__':
    main()
