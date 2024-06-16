import pyotp
import datetime

class TOTP:

    @staticmethod
    def generateTOTP(key, time, returnDigits, crypto='HmacSHA1'):
        totp = pyotp.TOTP(key, digits=int(returnDigits), digest=getattr(pyotp.utils, crypto.lower()))
        otp = totp.at(time)
        return otp

    @staticmethod
    def main():
        # Seed values for different HMAC algorithms
        seed = "3132333435363738393031323334353637383930"
        seed32 = "31323334353637383930313233343536373839303132333435363738393031323334"
        seed64 = "31323334353637383930313233343536373839303132333435363738393031323334" \
                 "313233343536373839303132333435363738393031323334"
        T0 = 0
        X = 30
        testTime = [59, 1111111109, 1111111111, 1234567890, 2000000000, 20000000000]

        print("+---------------+-----------------------+------------------+--------+--------+")
        print("|  Time(sec)    |   Time (UTC format)   | Value of T(Hex)  |  TOTP  | Mode   |")
        print("+---------------+-----------------------+------------------+--------+--------+")

        for t in testTime:
            T = (t - T0) // X
            steps = hex(T)[2:].upper().zfill(16)
            fmtTime = str(t).ljust(11)
            utcTime = datetime.datetime.utcfromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')
            print(f"|  {fmtTime}  |  {utcTime}  | {steps} | {TOTP.generateTOTP(seed, T, '8', 'HmacSHA1')} | SHA1   |")
            print(f"|  {fmtTime}  |  {utcTime}  | {steps} | {TOTP.generateTOTP(seed32, T, '8', 'HmacSHA256')} | SHA256 |")
            print(f"|  {fmtTime}  |  {utcTime}  | {steps} | {TOTP.generateTOTP(seed64, T, '8', 'HmacSHA512')} | SHA512 |")
            print("+---------------+-----------------------+------------------+--------+--------+")

if __name__ == "__main__":
    TOTP.main()
