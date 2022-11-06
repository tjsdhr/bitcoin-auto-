import pyupbit

access = "m0VbvS0ouv18ghPBs8rLVtlaBoHFjxScc0F3hSx5"         # 본인 값으로 변경
secret = "zPKFLqjrxblls2xBJNdfd8LTHIX4IXCxSRwgmubx"        # 본인 값으로 변경   
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회python test.py