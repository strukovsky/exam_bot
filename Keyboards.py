from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def active():
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('Спасибо', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button("Отписаться", color=VkKeyboardColor.NEGATIVE)
    return keyboard.get_keyboard()


def inactive():
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button("Включить", color=VkKeyboardColor.POSITIVE)
    return keyboard.get_keyboard()


def after_thanks():
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button("Отписаться", color=VkKeyboardColor.NEGATIVE)
    return keyboard.get_keyboard()
