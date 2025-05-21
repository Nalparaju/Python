#Mirror image of time

#input 02:35 and output 09:25

#%%
def timeReverse(h,m):
    if m > 0:
        h = 11-h
        m = 60-m
    else:
        h = 12-h
        m = 0
    
    return f"Reverse time is {h}:{m}"

print(timeReverse(2,35))
# %%
