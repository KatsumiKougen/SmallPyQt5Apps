import itertools

class VgVariant0():
    def __init__(self, key: str):
        self.key = key.lower()
        self.alp = "".join([chr(i) for i in range(97, 123)])
    
    def __repr__(self) -> str:
        return f"<Vigenère cipher class, key: \"{self.key}\">"
    
    def _CycleThrough(self, string: str, count: int) -> str:
        c = 0
        out = ""
        for i in itertools.cycle(string):
            if c < count:
                out += i
                c += 1
            else:
                break
        return out

    def encode(self, text: str) -> str:
        e = lambda OriginalChar, KeyChar: self.alp[(self.alp.index(OriginalChar.lower())+self.alp.index(KeyChar))%len(self.alp)]
        out = ""
        idx = 0
        key = self._CycleThrough(self.key, len(text))
        for char in text:
            if char.islower() and char.isalpha():
                out += e(char, key[idx])
                idx += 1
            elif char.isupper() and char.isalpha():
                out += e(char, key[idx]).upper()
                idx += 1
            else:
                out += char
        return out
    
    def decode(self, text: str) -> str:
        d = lambda CipherChar, KeyChar: self.alp[(self.alp.index(CipherChar.lower())-self.alp.index(KeyChar))%len(self.alp)]
        out = ""
        idx = 0
        key = self._CycleThrough(self.key, len(text))
        for char in text:
            if char.islower() and char.isalpha():
                out += d(char, key[idx])
                idx +=1
            elif char.isupper() and char.isalpha():
                out += d(char, key[idx]).upper()
                idx +=1
            else:
                out += char
        return out

class VgVariant1:
    def __init__(self, key: str | bytes | list[int, ...]):
        if isinstance(key, str):
            self.key = bytes(key, "utf-8")
        else:
            self.key = bytes(key)
        self.alp = [i for i in range(256)]
    
    def __repr__(self) -> str:
        return f"<8-bit Vigenère-RC4 cipher class, key: \"{self.key}\">"
    
    def _CycleThrough(self, bytes_: str | bytes | list[int, ...], count: int) -> list[int, ...]:
        c = 0
        out = []
        for i in itertools.cycle(bytes_):
            if c < count:
                if isinstance(i, str):
                    out.append(ord(i))
                elif isinstance(i, bytes):
                    out.append(int(i))
                else:
                    out.append(i)
                c += 1
            else:
                break
        return out

    def encode(self, text: str, readable: bool = True) -> str:
        e = lambda OriginalChar, KeyChar: self.alp[(self.alp.index(ord(OriginalChar))+self.alp.index(KeyChar))%len(self.alp)]
        out = []
        idx = 0
        key = self._CycleThrough(self.key, len(text))
        for char in text:
            out.append(e(char, key[idx]))
            idx += 1
        return repr(bytes(out)) if readable else bytes(out)
    
    def decode(self, text: str, readable: bool = True) -> str:
        d = lambda CipherChar, KeyChar: self.alp[(self.alp.index(ord(CipherChar))-self.alp.index(KeyChar))%len(self.alp)]
        out = []
        idx = 0
        key = self._CycleThrough(self.key, len(text))
        for char in text:
            out.append(d(char, key[idx]))
            idx += 1
        return repr(bytes(out)) if readable else bytes(out)

if __name__ == "__main__":
    test = VgVariant0("stnlymbl")
    print(test.encode("THE ORIGINAL MYSTERY TWINS"))
    test = VgVariant1("stnlymbl")
    print(test.encode("THE ORIGINAL MYSTERY TWINS"))
