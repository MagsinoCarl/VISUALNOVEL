# Declare characters used by this game.
define e = Character("Carl Cems", color="0000FF")
define j = Character("Matt", color="008000")
 
# The game starts here.
label start:

    scene bg_room

    # First scene: Carl on left, Jeppy not yet shown
    show carl normal at left with dissolve
    e "Matt... please. Just hear me out."                       

    # Show Jeppy at right
    show matt normal at right with dissolve
    j "Hear you out? After you threw everything away like it was nothing?"

    # Carl speaks again (still normal)
    show carl uniform sad1 at left with dissolve
    e "I made a mistake. I was scared, I thought it was better to end it before I got hurt worse."

    # Jeppy speaks again
    show matt normal at right with dissolve
    j "And what about me, Carl? Did you even think about what you were doing to me?"

    # Carl switches to "cry" expression (still on left)
    show carl uniform cry1 at left with dissolve
    e "I thought I was protecting us. I thought you'd be better off without me."

    # Jeppy switches to "cry" too (still on right)
    show matt uniform sad1 at right with dissolve
    j "You didn't even give me a choice. You decided for both of us."

    # Carl speaks while still crying
    show carl uniform cry2 at left with dissolve
    e "I'm sorry... I'm sorry, Matt. I was stupid. I regret it every second. I just... I just want you back."
    
    # Jeppy replies still crying
    show matt uniform sad2 at right with dissolve
    j "It's not that easy, Carl. You broke something. And I don't know if I can just pretend it never happened."

    # Carl begging
    show carl uniform cry3 at left with dissolve
    e "I don't want to pretend. I want to fix it. Please... just tell me what to do."

    # ---- Here's the CHOICE ----
    menu:
        "What will Matt do?"

        "Give Carl another chance":
            jump forgive_carl

        "Walk away from Carl":
            jump leave_carl
    # ----------------------------

# If the player chooses to forgive Carl
label forgive_carl:
    
    show matt uniform sad1 at right
    j "Maybe... maybe we can try again. But you have to promise me, Carl. No more running."

    show carl uniform cry4 at left
    e "I promise. I'll never leave again. Thank you, Matt..."

    # You can continue the happy scene here
    return

# If the player chooses to leave Carl
label leave_carl:

    show matt uniform sad1 at right
    j "I'm sorry, Carl. But I can't do this anymore. Goodbye."

    show carl uniform cry4 at left
    e "Jeppy... please..."

    # Fade to black or sad ending
    scene black with fade
    "Carl was left standing alone."

    scene bg school
 
    return
