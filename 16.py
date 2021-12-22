with open("16.txt", "r") as f:
    packet = bytes.fromhex(f.readline().strip())

class PacketParser:
    def __init__(self, data):
        self.data = data
        self.offset = 0
        self.version_sum = 0

    def advance(self, n=1):
        b = 0
        for _ in range(n):
            b <<= 1
            b |= (self.data[self.offset // 8] >> (8-self.offset%8-1)) & 0x01
            self.offset += 1
        return b

    def packet(self):
        version, type_id = self.advance(3), self.advance(3)
        self.version_sum += version
        if type_id == 4:
            literal = 0
            tag = 1
            while tag != 0:
                tag = self.advance()
                literal <<= 4
                literal |= self.advance(4)
            return literal
        else:
            results = []
            if self.advance() == 0:
                byte_length = self.advance(15)
                offset_start = self.offset
                while self.offset - offset_start < byte_length:
                    results.append(self.packet())
            else:
                packet_length = self.advance(11)
                for _ in range(packet_length):
                    results.append(self.packet())
            if type_id == 0:
                return sum(results)
            elif type_id == 1:
                result = 1
                for r in results:
                    result *= r
                return result
            elif type_id == 2:
                return min(results)
            elif type_id == 3:
                return max(results)
            elif type_id == 5:
                return int(results[0] > results[1])
            elif type_id == 6:
                return int(results[0] < results[1])
            elif type_id == 7:
                return int(results[0] == results[1])


parser = PacketParser(packet)
value = parser.packet()
print(parser.version_sum)
print(value)