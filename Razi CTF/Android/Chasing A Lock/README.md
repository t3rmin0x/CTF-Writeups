# Chasing a lock
> Points: 858

## Description
> as locks are so popular many will chase them but why? maybe a flag :)

## Solution
The app shows locks🔒 at random positions for a very short time interval... If we click the lock 20,000 times it will trigger something.
Decompiled the APK with jadx-gui. The Main Activity calls a class named `switcher` this assembles the flag from 5 functions.
```java
public class switcher {
    public String run(int i) {
        if (i != 0) {
            return null;
        }
        a1 a1Var = new a1();
        a2 a2Var = new a2();
        System.out.println(a2Var.run(i));
        String str = (" " + a1Var.run(i)) + a2Var.run(i);
        a3 a3Var = new a3();
        String str2 = str + a3Var.run(i);
        a4 a4Var = new a4();
        String str3 = str2 + a4Var.run(i);
        a5 a5Var = new a5();
        return str3 + a5Var.run(i);
    }
}
```
### Function a1
```java
public class a1 {
    public String run(int i) {
        String str = "Vm0wd2QyUXlVWGxWV0d4V1YwZDRWMVl3WkRSV01WbDNXa1JTVjAxV2JETlhhMUpUVmpBeFYySkVUbGhoTVVwVVZtcEJlRll5U2tWVWJHaG9UVlZ3VlZadGNFSmxSbGw1VTJ0V1ZXSkhhRzlVVmxaM1ZsWmFkR05GU214U2JHdzFWVEowVjFaWFNraGhSemxWVm14YU0xWnNXbUZqVmtaMFVteFNUbUpGY0VwV2JURXdZVEZrU0ZOclpHcFRSVXBZV1ZSR2QyRkdjRmRYYlVaclVsUkdWbFpYZUZOVWJVWTJVbFJHVjJFeVVYZFpla3BIWXpGT2RWVnRhRk5sYlhoWFZtMXdUMVF3TUhoalJscFlZbFZhY2xWcVFURlNNV1J5VjJ4T1ZXSlZjRWRaTUZaM1ZqSktWVkpZWkZkaGExcFlXa1ZhVDJNeFpITmhSMnhUVFcxb1dsWXhaRFJpTWtsNVZtNU9WbUpHV2xSWmJGWmhZMVphZEdSSFJrNVNiRm93V2xWYVQxWlhTbFpqUldSYVRVWmFNMVpxU2t0V1ZrcFpXa1p3VjFKV2NIbFdWRUpoVkRKT2MyTkZhR3BTYXpWWVZXcE9iMkl4V1hoYVJGSldUVlZzTlZaWE5VOVhSMHBJVld4c1dtSkdXbWhaTW5oWFkxWkdWVkpzVGs1V01VbzFWbXBKTVdFeFdYZE5WVlpUWVRGd1YxbHJXa3RUUmxweFVtMUdVMkpWYkRaWGExcHJZVWRGZUdOSE9WZGhhMHBvVmtSS1QyUkdTbkpoUjJoVFlYcFdlbGRYZUc5aU1XUkhWMjVTVGxOSFVuTlZha0p6VGtaVmVXUkhkRmhTTUhCSlZsZDRjMWR0U2tkWGJXaGFUVzVvV0ZsNlJsZGpiSEJIV2tkc1UySnJTbUZXTW5oWFdWWlJlRmRzYUZSaVJuQlpWbXRXZDFZeGJISlhhM1JVVW14d2VGVnRNVWRWTWtwV1lrUmFXR0V4Y0hKWlZXUkdaVWRPU0U5V1pHaGhNSEJ2Vm10U1MxUXlVa2RUYmtwaFVtMW9jRlpxU205bGJHUllaVWM1YVUxcmJEUldNV2h2V1ZaS1IxTnVRbFZXTTFKNlZHdGFZVk5IVWtoa1JtUnBWbGhDU1ZacVNqUlZNV1IwVTJ0a1dHSlhhR0ZVVnpWdlYwWnJlRmRyWkZkV2EzQjZWa2R6TVZZd01WWmlla1pYWWxoQ1RGUnJXbEpsUm1SellVWlNhVkp1UW5oV1YzaHJWVEZzVjFWc1dsaGlWVnBQVkZaYWQyVkdWWGxrUkVKWFRWWndlVmt3V25kWFIwVjRZMFJPV21FeVVrZGFWM2hIWTIxS1IxcEhiRmhTVlhCS1ZtMTBVMU14VlhoWFdHaFlZbXhhVmxsclpHOWpSbHB4VTIwNWJHSkhVbGxhVldNMVlWVXhjbUpFVWxkTmFsWlVWa2Q0YTFOR1ZuTlhiRlpYVFRGS05sWkhlR0ZXTWxKSVZXdG9hMUl5YUhCVmJHaENaREZhYzFwRVVtcE5WMUl3VlRKMGExZEhTbGhoUjBaVlZucFdkbFl3V25KbFJtUnlXa1prVjJFelFqWldhMlI2VFZaa1IxTnNXbXBTVjNoWVdXeG9RMVJHVW5KWGJFcHNVbTFTZWxsVldsTmhSVEZ6VTI1b1YxWjZSVEJhUkVaclVqSktTVlJ0YUZOaGVsWlFWa1phWVdReVZrZFdXR3hyVWtWS1dGUldXbmRsVm10M1YyNWtXRkl3VmpSWk1GSlBWMjFGZVZWclpHRldNMmhJV1RJeFMxSXhjRWhpUm1oVFZsaENTMVp0TVRCVk1VMTRWbGhvV0ZkSGFGbFpiWGhoVm14c2NscEhPV3BTYkhCNFZUSXdOV0pIU2toVmJHeGhWbGROTVZsV1ZYaGpiVXBGVld4a1RtRnNXbFZXYTJRMFlURk9SMVp1VGxoaVJscFlXV3RvUTFkV1draGxSMFpYVFd4S1NWWlhkRzloTVVwMFZXczVWMkZyV2t4Vk1uaHJWakZhZEZKdGNFNVdNVWwzVmxSS01HRXhaRWhUYkdob1VqQmFWbFp1Y0Zka2JGbDNWMjVLYkZKdFVubFhhMXByVmpKRmVsRnFXbGRoTWxJMlZGWmFXbVF3TVZkWGJXeHNZVEZ3V1ZkWGVHOVJNVkpIVlc1S1dHSkZjSE5WYlRGVFpXeHNWbGRzVG1oV2EzQXhWVmMxYjFZeFdYcGhTRXBYVmtWYWVsWnFSbGRqTVdSellVZHNWMVp1UWpaV01XUXdXVmRSZVZaclpGZFhSM2h5Vld0V1MxZEdVbGRYYm1Sc1ZteHNOVnBWYUd0WFIwcEhZMFpvV2sxSFVuWldNbmhoVjBaV2NscEhSbGRXTVVwUlZsZHdTMUl4U1hsU2EyaHBVbXMxY0ZsVVFuZE5iRnAwVFZSQ1ZrMVZNVFJXVm1oelZtMUZlVlZzV2xwaVdGSXpXVlZhVjJSSFZrWmtSM0JUWWtoQ05GWnJZM2RPVm1SSFYyNU9hbEp0ZUdGVVZWcFdUVlpzVjFaWWFHcGlWWEJHVmxkNGExUnRSbk5YYkZaWVZtMVJNRlY2Um1GamF6VlhZa1pLYVZKc2NGbFhWM1JoWkRGa1YxZHJhR3RTTUZwdlZGZHpNV1ZzV1hsT1ZrNW9UVlZzTlZsVmFFTldiVXBJWVVWT1lWSkZXbWhaZWtaM1VsWldkR05GTlZkTlZXd3pWbXhTUzAxSFJYaGFSV2hVWWtkb2IxVnFRbUZXYkZwMFpVaGtUazFXY0hsV01qRkhZV3hhY21ORVFtRlNWMUYzVm1wS1MyTnNUbkpoUm1SVFRUSm9iMVpyVWt0U01WbDRWRzVXVm1KRlNsaFZiRkpYVjFaYVIxbDZSbWxOVjFKSVdXdGFWMVZzWkVoaFJsSlZWbTFTVkZwWGVITldiR1J6Vkcxb1UxWkZXalpXVkVreFlqRlplRmRZY0ZaaVIyaFpWbTE0ZDFsV2NGWlhiWFJyVm10d2VsWnRNWE5XTVVsNllVUldWMDFYVVhkWFZtUlNaVlphY2xwR1pHbGlSWEI1VmxkMFYxTXlTWGhpUm14cVVsZFNjMVp0ZUV0bGJGcDBUVVJXV0ZJd2NFaFpNRnB2VjJzeFNHRkZlRmROYm1ob1ZqQmFWMk5zY0VoU2JHUk9UVzFvU2xZeFVrcGxSazE0VTFob2FsSlhVbWhWYlhNeFYwWlpkMVpyZEU1aVJuQXdXVEJXYTFkc1dYZFdhbEpYWWtkb2RsWXdXbXRUUjBaSFYyeHdhVmRIYUc5V2JURTBZekpPYzFwSVNtdFNNMEpVV1d0YWQwNUdXbGhOVkVKT1VteHNORll5TlU5aGJFcFlZVVpvVjJGck5WUldSVnB6VmxaR1dXRkdUbGRoTTBJMlZtdGtORmxXVlhsVGExcFlWMGhDV0Zac1duZFNNVkY0VjJ0T1ZtSkZTbFpVVlZGM1VGRTlQUT09";
        int i2 = 0;
        while (i2 < 20) {
            i2++;
            str = new String(Base64.decode(str.getBytes(), 0));
        }
        return str;
    }
}
```
Decoding the base64 string 19 times gives `RaziCTF`

### Function a2
```java
public class a2 {
    public String run(int i) {
        return xorHex("787d6c7f2c352b2c", "313333376d616e73313333376861");
    }

    public String xorHex(String str, String str2) {
        char[] cArr = new char[str.length()];
        int i = 0;
        for (int i2 = 0; i2 < cArr.length; i2++) {
            cArr[i2] = toHex(fromHex(str.charAt(i2)) ^ fromHex(str2.charAt(i2)));
        }
        StringBuilder sb = new StringBuilder();
        while (i < new String(cArr).length()) {
            int i3 = i + 2;
            sb.append((char) Integer.parseInt(new String(cArr).substring(i, i3), 16));
            i = i3;
        }
        return "{" + sb.toString().trim();
    }
```
It xors `0x787d6c7f2c352b2c` with `0x313333376d616e73313333376861` and decodes from hex and gives `{IN_HATE_`

### Function a3
```java
public class a3 {
    public String run(int i) {
        int i2 = (i % 100000) / 2;
        return (i2 - i2) + "F";
    }
}
```
Returns `0F`

### Function a4
```java
public class a4 {
    public String run(int i) {
        return "_RUNN";
    }
}
```
Returns `_RUNN`

### Function a5
This is the most complicated function jadx can't decompile most of it's code. The interesting parts are...
```java
java.lang.String r0 = "="
            java.lang.String r1 = "%"
            java.lang.String r2 = "!"
            java.lang.String[] r2 = new java.lang.String[]{r2, r1, r0}
            java.lang.String r3 = "a"
            java.lang.String r4 = "b"
            java.lang.String r5 = "N"
            java.lang.String[] r4 = new java.lang.String[]{r3, r4, r5}
            java.lang.String r5 = "1"
            java.lang.String r6 = "G"
            java.lang.String r7 = "2"
            java.lang.String[] r5 = new java.lang.String[]{r5, r6, r7}
            java.lang.String r6 = "_"
            java.lang.String[] r1 = new java.lang.String[]{r6, r1, r0}
            java.lang.String r0 = "A"
            java.lang.String r6 = "L"
            java.lang.String r7 = "D"
            java.lang.String[] r6 = new java.lang.String[]{r0, r6, r7}
            java.lang.String r7 = "0"
            java.lang.String r0 = "R"
            java.lang.String r8 = "$"
            java.lang.String[] r8 = new java.lang.String[]{r0, r7, r8}
            java.lang.String r0 = "C"
            java.lang.String r9 = "q"
            java.lang.String r10 = "3"
            java.lang.String[] r9 = new java.lang.String[]{r0, r9, r10}
            java.lang.String r0 = "K"
            java.lang.String r10 = "4"
            java.lang.String r11 = "("
            java.lang.String[] r10 = new java.lang.String[]{r10, r0, r11}
            java.lang.String r11 = "5"
            java.lang.String r12 = "J"
            java.lang.String[] r11 = new java.lang.String[]{r11, r12, r0}
            java.io.PrintStream r0 = java.lang.System.out
            r0.println(r3)
            .....
            if (r9 >= r13) goto L_0x015e
            java.lang.StringBuilder r0 = new java.lang.StringBuilder
            r0.<init>()
            r13 = r2[r12]
            r0.append(r13)
            r13 = r4[r14]
            r0.append(r13)
            r13 = r5[r15]
            r0.append(r13)
            r13 = r1[r3]
            r0.append(r13)
            r13 = r6[r7]
            r0.append(r13)
            r13 = r8[r11]
            r0.append(r13)
            r13 = r19[r10]
            r0.append(r13)
            r13 = r18[r20]
            r0.append(r13)
            r13 = r17[r9]
            r0.append(r13)
            java.lang.String r0 = r0.toString()
            java.lang.StringBuilder r13 = new java.lang.StringBuilder
            r13.<init>()
            r13.append(r0)
            java.lang.String r0 = "}"
            r13.append(r0)
            java.lang.String r0 = r13.toString()
            java.io.PrintStream r13 = java.lang.System.out

```
The code is too complicated to understand.. So I applied some common sonse... `RUNN` must mean `RUNNING` which becomes `RUNN!NG_`.
After that I bruteforced the last 5 digits and searched for meaningful word. Generated a simple wordlist for indices with crunch for bruteforce `crunch 5 5 012 > combi`
```py
arr1 = ["A", "L", "D"]
arr2 = ["0", "R", "$"]
arr3 = ["C", "q", "3"]
arr4 = ["K", "4", "("]
arr5 = ["K", "5", "J"]

f = open("combi")
lines = f.readlines()
for line in lines:
    combination = (line.strip())
    junk = []
    for i in combination:
        junk.append(int(i))
    flag = ""
    flag += str(arr1[junk[0]])
    flag += str(arr2[junk[1]])
    flag += str(arr3[junk[2]])
    flag += str(arr4[junk[3]])
    flag += str(arr5[junk[4]])
    print(flag)
```
The meaningful word is `L0CK5`
So the total return is `!NG_L0CK5}`
## Flag
> RaziCTF{IN_HATE_0F_RUNN!NG_L0CK5}
