


int_contents = []
def calculus():
    suma = 0;
    with open("data.txt",'r') as file:
        contents = file.readlines()
            # print(contents)

    for i in range(0,len(contents)):
         int_contents.append(int(str(contents[i]).strip()))
    ok=True;

    for i in range(0,len(int_contents)):
        ok=True;
        while ok:
            temp=(int)(int_contents[i]/3)-2;
            if(temp>=0):
                suma+=temp;
                int_contents[i]=temp;
            else :
                ok=False;
    print(int(suma))



    # for i in int_contents:
    #     suma+=(int)(int_contents[i]/3)-2
    #
    # print(suma);

calculus();