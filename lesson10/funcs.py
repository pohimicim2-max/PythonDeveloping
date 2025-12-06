import data

score = 0
quest_index = 0
quests_data = data.questions

def generate_quest(QUEST, buttons):
    if quest_index < len(quests_data):
        quest = quests_data[quest_index]["quest"]
        QUEST.config(text=quest)
        for i in range(len(buttons)):
            buttons[i].config(text=quests_data[quest_index]["answers"][i])
    else:
        QUEST.config(text=f"Викторина окончена! Счёт: {score}/5")
        for btn in buttons:
            btn.config(state="disabled")

def choice(button, QUEST, buttons, info):
    global quest_index
    if button["text"] == quests_data[quest_index]["right"]:
        quest_index += 1
        info.config(text="")
        generate_quest(QUEST, buttons)
    else:
        info.config(text="Неправильно")
def check_answer(selected_index):
    global quest_index, score
    correct_answer_index = quests_data[quest_index]["correct"]
    if selected_index == correct_answer_index:
        score += 1


