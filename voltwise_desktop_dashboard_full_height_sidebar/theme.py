from nicegui import ui

class Theme:
    """
    Centraliseret Tailwind Design System.
    Samler alle genanvendelige stylingklasser på ét sted.
    Gør det meget nemmere at læse selve UI-koden, og tillader genbrug af
    designet på tværs af fremtidige sider og projekter.
    """

    @staticmethod
    def setup():
        """Indsætter Tailwind CDN, Google Fonts og basis styling."""
        ui.add_head_html('''
        <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
        <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet"/>
        <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
        <script id="tailwind-config">
            tailwind.config = {
                darkMode: "class",
                theme: {
                    extend: {
                        colors: {
                            "primary": "#0df259",
                            "primary-dark": "#0a8a35",
                            "background-light": "#f5f8f6",
                            "background-dark": "#102216",
                            "nordic-gray": "#e1e8e3",
                        },
                        fontFamily: {
                            "display": ["Manrope", "sans-serif"]
                        },
                        borderRadius: {
                            "DEFAULT": "0.5rem",
                            "lg": "1rem",
                            "xl": "1.25rem",
                            "full": "9999px"
                        },
                    },
                },
            }
        </script>
        <style>
            .status-glow { background: radial-gradient(circle, rgba(13, 242, 89, 0.15) 0%, rgba(255, 255, 255, 0) 70%); }
            body { font-family: 'Manrope', sans-serif; -webkit-font-smoothing: antialiased; }
            .material-symbols-outlined { font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24; display: inline-block; vertical-align: middle; }
        </style>
        ''')
        ui.query('body').classes('bg-white text-[#0d1c12] m-0 p-0 font-["Manrope"]')
        ui.query('.q-page-container').classes('p-0 m-0')
        ui.query('.q-page').classes('min-h-screen')

    # ==========================================
    # LAYOUT STRUKTUR
    # ==========================================
    LAYOUT_ROOT     = 'min-h-screen flex h-screen overflow-hidden w-full'
    LAYOUT_SIDEBAR  = 'w-72 bg-[#f8faf9] border-r border-nordic-gray h-screen sticky top-0 flex flex-col p-8 flex-shrink-0'
    LAYOUT_MAIN     = 'mx-auto px-8 lg:px-12 py-6 flex-1 h-full overflow-y-auto'
    LAYOUT_GRID     = 'grid grid-cols-1 lg:grid-cols-12 gap-12'

    # ==========================================
    # TYPOGRAFI
    # ==========================================
    H1              = 'text-2xl font-extrabold tracking-tight'
    H2              = 'text-7xl font-black tracking-tighter text-[#0d1c12]'
    H3              = 'text-2xl font-bold mb-1'
    H4              = 'text-lg font-bold mb-4'
    TEXT_MUTED      = 'text-gray-500'
    TEXT_MUTED_SM   = 'text-gray-500 text-sm'
    TEXT_STRONG     = 'font-bold text-[#0d1c12]'

    # ==========================================
    # KOMPONENTER & KORT
    # ==========================================
    CARD            = 'bg-white border border-nordic-gray rounded-xl p-6 flex flex-col hover:shadow-xl hover:shadow-primary/5 transition-all'
    WIDGET_PANEL    = 'bg-background-light p-8 rounded-xl flex items-center justify-between'
    SIDEBOX         = 'bg-background-light rounded-xl p-8 border border-nordic-gray sticky top-8'
    HERO_BANNER     = 'relative py-20 rounded-xl flex flex-col items-center justify-center text-center status-glow'

    # ==========================================
    # NAVIGATION & LINKS
    # ==========================================
    NAV_BASE        = 'flex items-center gap-3 px-4 py-3 rounded-xl transition-colors'
    NAV_ACTIVE      = 'bg-primary/10 text-primary-dark font-bold'
    NAV_INACTIVE    = 'text-gray-500 hover:bg-background-light hover:text-[#0d1c12] font-semibold'
    LINK_PRIMARY    = 'text-primary-dark font-bold text-sm flex items-center gap-1 hover:underline cursor-pointer'

    # ==========================================
    # KNAPPER
    # ==========================================
    BTN_DARK        = 'flex items-center gap-2 bg-[#0d1c12] text-white !px-8 !py-4 !min-h-0 rounded-xl font-bold hover:scale-105 transition-transform'
    BTN_PRIMARY     = 'bg-primary text-[#0d1c12] !px-8 !py-3 !min-h-0 rounded-xl font-bold flex items-center gap-2 hover:scale-105 transition-transform'
    BTN_BLOCK_DARK  = 'w-full bg-[#0d1c12] text-white py-3 rounded-lg font-bold hover:bg-opacity-90 transition-colors text-center cursor-pointer'
    BTN_BLOCK_LIGHT = 'w-full mt-10 bg-white border border-nordic-gray py-3 rounded-lg text-sm font-bold hover:bg-gray-50 transition-colors text-center cursor-pointer block'
    BTN_ICON        = '!p-2 hover:bg-background-light rounded-full transition-colors'

    # ==========================================
    # IKONER & GRAFIK
    # ==========================================
    ICON            = 'material-symbols-outlined'
    ICON_BOX        = 'w-12 h-12 bg-background-light rounded-lg flex items-center justify-center mb-6 text-primary-dark'
    ICON_CIRCLE     = 'w-16 h-16 bg-white rounded-full flex items-center justify-center shadow-sm text-yellow-500 text-4xl'
    AVATAR          = 'w-10 h-10 rounded-full bg-nordic-gray overflow-hidden border border-nordic-gray bg-cover'

    # ==========================================
    # BADGES & PROGRESS
    # ==========================================
    BADGE_LITE      = 'inline-flex items-center gap-2 px-3 py-1 bg-primary/20 rounded-full border border-primary/30 text-xs font-bold uppercase tracking-widest text-primary-dark'
    BADGE_FILLED    = 'bg-primary/10 border border-primary/30 text-primary-dark text-xs font-bold py-1 px-3 rounded-full w-fit'
    PROGRESS_BG     = 'mt-4 h-2 bg-nordic-gray rounded-full overflow-hidden'
    PROGRESS_FILL   = 'bg-primary h-full'
