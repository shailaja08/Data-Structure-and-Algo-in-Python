def vol(st):
    vol=set("aeiou")
    s=set({})
    st=st.lower()
    for char in st:
        if char in vol:
            s.add(char)
        else:
            pass
    print(s)
    if len(s)==len(vol):
        print("accepted")
    else:
        print("rejected")

st="ABeeIghiObhkUul"
vol(st)
