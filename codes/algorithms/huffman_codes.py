import heapq    #library to implement heaps

#generate frequencies of each character in the text
def generate_frequencies(text):
    freq = [0]*26
    for character in text:
        if character>='a' and character<='z':
            freq[ord(character)-ord('a')] += 1
    H=[]
    for f in freq:
        if f>0:
            H.append(f)
    return [H, freq]


class node:

    #defining structure of each node
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.data = None
        self.visited = 0
        self.code = None

    #encoding the tree generated
    def encode(node, dict, freq):
        if node.left==None:
            if node.parent.left.data==node.data and node.parent.left.visited==0:
                node.code = node.parent.code + '0'
                node.visited=1
            else:
                node.code = node.parent.code + '1'

            for i in range(len(freq)):
                if node.data == freq[i]:
                    dict[ord('a')+i] = node.code
                    freq[i]=0
                    break
            return

        if node.parent==None:
            node.code=''
        else:
            if node.parent.left.data==node.data and node.parent.left.visited==0:
                node.code = node.parent.code + '0'
                node.visited = 1
            else:
                node.code = node.parent.code + '1'
        node.left.encode(dict, freq)
        node.right.encode(dict, freq)

#generating the Huffman code tree
def generate_tree(H):
    heapq.heapify(H)
    root_vals=[]
    roots=[]
    while(len(H)>1):
        m = heapq.heappop(H)
        n = heapq.heappop(H)
        M = m
        N = n
        heapq.heappush(H, m+n)
        copy_vals = root_vals[:]
        flag=0
        for vals in copy_vals:
            if M==vals or N==vals:
                if M==vals:
                    M=-1
                else:
                    N=-1
                flag+=1
                vals=-2

        if flag==0:
            L = node()
            L.data = m
            R = node()
            R.data = n
            new = node()
            new.data = m+n
            new.left = L
            new.right = R
            L.parent=new
            R.parent=new
            roots.append(new)
            root_vals.append(m+n)

        if flag==2:
            L = node()
            R = node()
            for root in roots:
                if root.data == m:
                    L = root
                    roots.remove(root)
                    break
            for root in roots:
                if root.data == n:
                    R =  root
                    roots.remove(root)
                    break
            new = node()
            new.data = m+n
            new.left = L
            new.right = R
            L.parent=new
            R.parent=new
            roots.append(new)
            root_vals.remove(m)
            root_vals.remove(n)
            root_vals.append(m+n)

        if flag==1:
            L = node()
            R = node()
            for root in roots:
                if root.data==m or root.data==n:
                    L = root
                    R = node()
                    if L.data==m:
                        R.data=n
                    else:
                        R.data=m
                    new = node()
                    new.data=m+n
                    new.left=L
                    new.right=R
                    L.parent=new
                    R.parent=new
                    roots.append(new)
                    roots.remove(root)
                    root_vals.remove(L.data)
                    root_vals.append(m+n)
                    break
    return roots[0]

#encoding using the functions defined above
text = input("Enter a piece of text: ")
text = text.lower()
H = generate_frequencies(text)[0]
freq = generate_frequencies(text)[1]
root = generate_tree(H)
dict = {}
root.encode(dict, freq)

#printing section
print("Encoding is:")
for x, y in dict.items():
    print(chr(x), "=", y)
print("\nEncoded message: ")
for character in text:
    if character>='a' and character<='z':
        print(dict[ord(character)], end="")
