from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def hdr(icon, title):
    return f"<b>{icon} {title}</b>"

class K:
    @staticmethod
    def back_admin():
        return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="« Back", callback_data="a_maint")]
        ])

    @staticmethod
    def admin(user_id):
        return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="📢 Broadcast", callback_data="a_bcast_menu")],
            [InlineKeyboardButton(text="💎 Add VIP", callback_data="a_addvip"), InlineKeyboardButton(text="❌ Remove VIP", callback_data="a_rmvip")],
            [InlineKeyboardButton(text="ℹ User Profile", callback_data="a_profile")],
            [InlineKeyboardButton(text="🔧 Maintenance", callback_data="a_maint")]
        ])
