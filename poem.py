import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    
def display_menu():
    # Display the menu options
    print("Menu:")
    print("1. twinkle_twinkle")
    print("2. jhonny_jhonny")
    print("3. nani_teri_morni")
    print("4. lakdi_ki_kathi")

def twinkle_twinkle ():
    text = """Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.
"""
    print(text)
    speak(text)

def jhonny_jhonny():
    
    text="""Johny, Johny!
Yes papa?
Eating sugar?
No papa.
Telling lies?
No papa.
Open your mouth!
Ha ha ha! """
    print(text)
    speak(text)

def nani_teri_morni():
   
    text = """नानी तेरी मोरनी को मोर ले गए,
बाकी जो बचा था काले चोर ले गए।

नानी तेरी मोरनी को मोर ले गए,
बाकी जो बचा था काले चोर ले गए।

एक मोटा मोटा ताला था,
ताले में से झपका लाले लाल करारे गेहुएं।

नानी तेरी मोरनी को मोर ले गए,
बाकी जो बचा था काले चोर ले गए।

घड़ी की टिक टिक में,
सब कुछ हो गया,
मोरनी रोई चिल्लाई,
पर कोई नहीं आया।

नानी तेरी मोरनी को मोर ले गए,
बाकी जो बचा था काले चोर ले गए।
"""
    print(text)
    speak(text)
def lakdi_ki_kathi():
    text = """लकड़ी की काठी, काठी पे घोड़ा,
घोड़े की दुम पे जो मारा हथौड़ा।
दौड़ा दौड़ा दौड़ा घोड़ा, दुम उठाके दौड़ा।
दौड़ा दौड़ा दौड़ा घोड़ा, दुम उठाके दौड़ा।

लकड़ी की काठी, काठी पे घोड़ा,
घोड़े की दुम पे जो मारा हथौड़ा।

ठुमक ठुमक कर चली काठ की गुड़िया,
पानी में पड़ गई, पानी से डर गई।
सिसक सिसक के कहे काठ की गुड़िया,
हाय राम, हाय राम, पानी से डर गई।

लकड़ी की काठी, काठी पे घोड़ा,
घोड़े की दुम पे जो मारा हथौड़ा।
दौड़ा दौड़ा दौड़ा घोड़ा, दुम उठाके दौड़ा।
दौड़ा दौड़ा दौड़ा घोड़ा, दुम उठाके दौड़ा।
"""
    print(text)
    speak(text)
   
def main():   
    while True:    
        display_menu()

      
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            twinkle_twinkle()
        elif choice == '2':
            jhonny_jhonny()
        elif choice == '3':
            nani_teri_morni
            ()
        elif choice == '4':
            lakdi_ki_kathi()
            break
        else:
            print("kuch dhang ka type krrde")
            
       


if __name__ == "__main__":
    main()
