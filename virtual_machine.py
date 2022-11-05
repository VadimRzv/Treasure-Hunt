class VirtualMachine():
    memory = {
        '000000': '00000000'
    }

    def virtual_machine(self, instruction:str):
        if self.memory.get(instruction[2:]) == None:
            self.memory[instruction[2:]] = '00000000'
            
        if   instruction[:3] == '00':
            self.incrementation()
        elif instruction[:3] == '01':
            self.decrementation()
        elif instruction[:3] == '10':
            self.jump()
        elif instruction[:3] == '11':
            self.output

        print(self.memory)
        ...

    def incrementation(self):     #00xxxxxx
        ...

    def decrementation(slef):     #01xxxxxx
        ...

    def jump(self):               #10xxxxxx
        ...

    def output(self):             #11xxxxxx
        ...


virt = VirtualMachine()

virt.virtual_machine('00000001')