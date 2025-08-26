# One hint

## Chalange

- Bài này gửi một file enc.txt từ flag và file main để sinh mã:
- [enc.txt](https://github.com/TemmaVN/LitCTF/blob/main/Crypto/One_hint/enc.txt)
- [main.py](https://github.com/TemmaVN/LitCTF/blob/main/Crypto/One_hint/main.py)

## Solution

- Mật mã gần như mã Vinegere cơ bản, nhưng được lặp lại rất nhiều lần nên việc giải thiên về số học.
- Để ý trong hàm vinegere: 
```
    res += chr((ord(pt[i])+ord(key[i%len(key)])-2*ord('a'))%26+ord('a'))
```
- Từ đó suy ra mỗi kí tự sẽ được mã hóa tuyến tính dạng: y = x + k (với k là khóa)
- Ta xem trong hàm pow:
```
    a = vigenere(a, vigenere(a, a))
```
- Sau mỗi vòng sẽ tuyến tính dạng y = x + (x + x)  = 3x
- Và sau n lần : y = x * 3**n
- Công việc đơn giản là tính (3**n) **-1 (mod 26) cho từ kí tự là ra!
- Tham khảo script giải: [solve.py](https://github.com/TemmaVN/LitCTF/blob/main/Crypto/One_hint/solve.py)
- Và thu được flag : ```LITCTF{perhaps_the_weirdest_vigenere_ever}```