# Signs

## Challenge

- Một thử thách thú vị nhưng đơn giản lạ kì:
- [output.txt](https://github.com/TemmaVN/LitCTF/blob/main/Crypto/signs/output.txt)
- [gen.py](https://github.com/TemmaVN/LitCTF/blob/main/Crypto/signs/gen.py)

# Solution

- Với n dài 2048 bit và e = 0x10001 thì hầu như các loại tấn công cơ bản, ta sẽ phân tích dữ kiện thêm: 
```
    sign = pow(btl(hashing(flag, 256)), d, n)
    print(f"{sign = }")
```
- Hàm hashing cơ bản chỉ là pad (byte thêm là hash_sum - hash_byte ) vì d = inverse(d,t) nên ta chỉ pow(sign,e,n) là ra được flag + padding!!
- Script : [solve.py](https://github.com/TemmaVN/LitCTF/blob/main/Crypto/signs/solve.py) (Thề nó dễ không tưởng :)))
- Flag là : ```LITCTF{1m_s34ch1ng_f0r_4_n3w_h4sh1ng_func710n}```