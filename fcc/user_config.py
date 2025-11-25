


# 'd' stands for dictionary and 't' stands for tuple while 'st' stands for string in the functions 
def add_setting(d, t):
    s_key = t[0].lower()
    s_val = t[1].lower()

    #print(d, s_key, s_val)
    if s_key in d.keys():
      return f"Setting '{s_key}' already exists! Cannot add a new setting with this name."
    d[s_key] = s_val
    return f"Setting '{s_key}' added with value '{s_val}' successfully!"
    #return d

def update_setting(d, t):
  s_key = t[0].lower()
  s_val = t[1].lower()

  if s_key in d.keys():
    d[s_key] = s_val
    #print(d)
    return f"Setting '{s_key}' updated to '{s_val}' successfully!"
  
  return f"Setting '{s_key}' does not exist! Cannot update a non-existing setting."

def delete_setting(d, st):
  s_key = st.lower()
    
  if s_key in d.keys():
    del d[s_key]
    print(d)
    return f"Setting '{s_key}' deleted successfully!"

  return "Setting not found!"

def view_settings(d):
  if not d:
    return "No settings available."
  s = ''
  for key, value in d.items():
    s += f"{key.capitalize()}: {value}\n"

  return f"Current User Settings:\n{s}"

test_settings = {
    'theme': 'darkgreen',
    'language': 'English'
}
new_setting = ('theme', 'Gothic')

#print(add_setting(test_settings, new_setting))
#print(update_setting(test_settings, new_setting))
#print(delete_setting(test_settings, 'theme'))
print(view_settings(test_setti
