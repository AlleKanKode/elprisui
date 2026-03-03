from nicegui import ui

def setup_head():
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
        .status-glow {
            background: radial-gradient(circle, rgba(13, 242, 89, 0.15) 0%, rgba(255, 255, 255, 0) 70%);
        }
        body {
            font-family: 'Manrope', sans-serif;
            -webkit-font-smoothing: antialiased;
        }
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
    </style>
    ''')

def create_sidebar():
    with ui.element('aside').classes('w-72 bg-[#f8faf9] border-r border-nordic-gray h-screen sticky top-0 flex flex-col p-8 flex-shrink-0'):
        with ui.element('div').classes('flex items-center gap-3 mb-12'):
            with ui.element('div').classes('bg-primary p-2 rounded-lg shadow-sm'):
                ui.label('bolt').classes('material-symbols-outlined text-black block')
            ui.label('VoltWise').classes('text-2xl font-extrabold tracking-tight')
        
        with ui.element('nav').classes('flex-1 space-y-2'):
            with ui.link(target='#').classes('flex items-center gap-3 px-4 py-3 bg-primary/10 text-primary-dark rounded-xl font-bold transition-colors'):
                ui.label('dashboard').classes('material-symbols-outlined')
                ui.label('Dashboard')
            with ui.link(target='#').classes('flex items-center gap-3 px-4 py-3 text-gray-500 hover:bg-background-light hover:text-[#0d1c12] rounded-xl font-semibold transition-colors'):
                ui.label('history').classes('material-symbols-outlined')
                ui.label('Historik')
            with ui.link(target='#').classes('flex items-center gap-3 px-4 py-3 text-gray-500 hover:bg-background-light hover:text-[#0d1c12] rounded-xl font-semibold transition-colors'):
                ui.label('devices').classes('material-symbols-outlined')
                ui.label('Enheder')
            with ui.link(target='#').classes('flex items-center gap-3 px-4 py-3 text-gray-500 hover:bg-background-light hover:text-[#0d1c12] rounded-xl font-semibold transition-colors'):
                ui.label('person').classes('material-symbols-outlined')
                ui.label('Profil')
                
        with ui.element('div').classes('pt-8 border-t border-nordic-gray mt-auto'):
            with ui.link(target='#').classes('flex items-center gap-3 px-4 py-3 text-gray-500 hover:bg-background-light hover:text-[#0d1c12] rounded-xl font-semibold transition-colors'):
                ui.label('settings').classes('material-symbols-outlined')
                ui.label('Indstillinger')

def create_main_content():
    with ui.element('div').classes('mx-auto px-8 lg:px-12 py-6 flex-1 h-full overflow-y-auto'):
        # Header
        with ui.element('header').classes('flex items-center justify-between mb-12 w-full'):
            ui.element('div').classes('flex items-center gap-6')
            with ui.element('div').classes('flex items-center gap-4'):
                with ui.button(color=None).props('unelevated no-caps padding="none"').classes('p-2 hover:bg-background-light rounded-full transition-colors'):
                    ui.label('notifications').classes('material-symbols-outlined text-gray-600')
                ui.element('div').classes('w-10 h-10 rounded-full bg-nordic-gray overflow-hidden border border-nordic-gray').style("background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuCzYwTRHD7eBsRfu-BhXlfSEeOvNq0yeUEPwwhbowu1VHthaRqxOtG9tMgOnragTGNp0OtUGESb4POKChOsOT_FQkmmUNynqjGPPlrPY5vcqQbABA3H1G8AG2eQPaySxEGAUIh6c7pgAdLgAzpzn9bflXHK_yHLnvRXhEjr1R-7Wk3DH7Q_klqbYIAX9SEsvNXrQFl_eWacMHVSoRK3Xxj-jvBmofvDNLbGyQMiGH0fymIKg5p4OHFR2pf9Yx9dEdvygxzy704Q6Xo'); background-size: cover;")

        with ui.element('div').classes('grid grid-cols-1 lg:grid-cols-12 gap-12'):
            # Main Content Area
            with ui.element('main').classes('lg:col-span-9 space-y-16'):
                # Hero Section
                with ui.element('section').classes('relative py-20 rounded-xl flex flex-col items-center justify-center text-center status-glow'):
                    with ui.element('div').classes('mb-4 inline-flex items-center gap-2 px-3 py-1 bg-primary/20 rounded-full border border-primary/30'):
                        ui.element('span').classes('w-2 h-2 rounded-full bg-primary animate-pulse')
                        ui.label('Status: Grøn strøm netop nu').classes('text-xs font-bold uppercase tracking-widest text-primary-dark')
                    
                    with ui.element('div').classes('flex flex-col items-center'):
                        ui.label('Nuværende pris').classes('text-gray-500 font-medium mb-1')
                        with ui.element('h2').classes('text-7xl font-black tracking-tighter text-[#0d1c12]'):
                            ui.label('2,45').classes('inline')
                            ui.label('kr. pr. kWh').classes('text-3xl font-bold opacity-60 ml-2 inline')
                            
                    with ui.button(color=None).props('unelevated no-caps padding="none"').classes('mt-10 flex items-center gap-2 bg-[#0d1c12] text-white px-8 py-4 rounded-xl font-bold hover:scale-105 transition-transform'):
                        ui.label('refresh').classes('material-symbols-outlined')
                        ui.label('Opdater pris')
                
                # Smart Delay Section
                with ui.element('section'):
                    with ui.element('div').classes('flex items-center justify-between mb-8'):
                        with ui.element('div'):
                            ui.label('Smart Delay').classes('text-2xl font-bold mb-1')
                            ui.label('Optimér dit forbrug og spar penge ved at vente.').classes('text-gray-500')
                        with ui.button(color=None).props('unelevated no-caps padding="none" ripple="false"').classes('text-primary-dark font-bold text-sm flex items-center gap-1 hover:underline'):
                            ui.label('Se alle enheder')
                            ui.label('arrow_forward').classes('material-symbols-outlined text-sm')
                            
                    with ui.element('div').classes('grid grid-cols-1 md:grid-cols-3 gap-6'):
                        def create_card(icon, title, price_now, price_later, saving):
                            with ui.element('div').classes('bg-white border border-nordic-gray rounded-xl p-6 flex flex-col hover:shadow-xl hover:shadow-primary/5 transition-all'):
                                with ui.element('div').classes('w-12 h-12 bg-background-light rounded-lg flex items-center justify-center mb-6'):
                                    ui.label(icon).classes('material-symbols-outlined text-primary-dark')
                                ui.label(title).classes('text-lg font-bold mb-4')
                                with ui.element('div').classes('space-y-3 mb-8'):
                                    with ui.element('div').classes('flex justify-between text-sm'):
                                        ui.label('Start nu').classes('text-gray-500')
                                        ui.label(price_now).classes('font-semibold')
                                    with ui.element('div').classes('flex justify-between text-sm'):
                                        ui.label('Vent og spar').classes('text-gray-500')
                                        ui.label(price_later).classes('font-semibold text-primary-dark')
                                with ui.element('div').classes('mt-auto space-y-3'):
                                    ui.label(f'Spar {saving}').classes('bg-primary/10 border border-primary/30 text-primary-dark text-xs font-bold py-1 px-3 rounded-full w-fit')
                                    ui.label('Vent til kl. 01:00').classes('w-full bg-[#0d1c12] text-white py-3 rounded-lg font-bold hover:bg-opacity-90 transition-colors text-center')

                        create_card('dishwasher', 'Opvaskemaskine', '4,50 kr.', '1,20 kr.', '3,30 kr.')
                        create_card('dry_cleaning', 'Tørretumbler', '6,20 kr.', '2,10 kr.', '4,10 kr.')
                        create_card('ev_station', 'Elbil', '45,00 kr.', '15,50 kr.', '29,50 kr.')

                # Social Feature
                with ui.element('section').classes('bg-background-light p-8 rounded-xl flex items-center justify-between'):
                    with ui.element('div').classes('flex items-center gap-6'):
                        with ui.element('div').classes('w-16 h-16 bg-white rounded-full flex items-center justify-center shadow-sm'):
                            ui.label('emoji_events').classes('material-symbols-outlined text-4xl text-yellow-500')
                        with ui.element('div'):
                            ui.label('Har du en god grøn stime?').classes('text-xl font-bold')
                            ui.label('Del dine resultater og inspirér andre til at spare.').classes('text-gray-500')
                    with ui.button(color=None).props('unelevated no-caps padding="none"').classes('bg-primary text-black px-8 py-3 rounded-xl font-bold flex items-center gap-2 hover:scale-105 transition-transform'):
                        ui.label('share').classes('material-symbols-outlined')
                        ui.label('Del min besparelse')

            # Sidebar: Impact
            with ui.element('aside').classes('lg:col-span-3 space-y-8 h-full flex-shrink-0'):
                with ui.element('div').classes('bg-background-light rounded-xl p-8 border border-nordic-gray sticky top-8'):
                    with ui.element('h3').classes('text-xl font-bold mb-8 flex items-center gap-2'):
                        ui.label('monitoring').classes('material-symbols-outlined text-primary-dark')
                        ui.label('Din Impact')
                    
                    # Savings Money
                    with ui.element('div').classes('mb-10'):
                        with ui.element('div').classes('flex items-center gap-2 text-gray-500 text-sm mb-2'):
                            ui.label('savings').classes('material-symbols-outlined text-sm')
                            ui.label('Livstidsbesparelse')
                        with ui.element('div').classes('text-3xl font-black text-[#0d1c12]'):
                            ui.label('1.245,50 ').classes('inline')
                            ui.label('kr.').classes('text-lg font-bold opacity-60 inline')
                        with ui.element('div').classes('mt-4 h-2 bg-nordic-gray rounded-full overflow-hidden'):
                            ui.element('div').classes('bg-primary h-full w-[65%]').props('data-alt="Progress bar showing savings toward monthly goal"')
                        ui.label('65% af dit månedlige mål nået').classes('text-xs text-gray-500 mt-2 font-medium')

                    # CO2 Reduction
                    with ui.element('div').classes('mb-10'):
                        with ui.element('div').classes('flex items-center gap-2 text-gray-500 text-sm mb-2'):
                            ui.label('eco').classes('material-symbols-outlined text-sm')
                            ui.label('CO2-reduktion')
                        with ui.element('div').classes('text-3xl font-black text-[#0d1c12]'):
                            ui.label('342 ').classes('inline')
                            ui.label('kg.').classes('text-lg font-bold opacity-60 inline')
                        with ui.element('p').classes('text-xs text-gray-500 mt-2 font-medium'):
                            ui.label('Svarer til at plante ').classes('inline')
                            ui.label('14 træer').classes('text-primary-dark font-bold inline')
                            ui.label(' 🌲').classes('inline')

                    # Stats Breakdown
                    with ui.element('div').classes('space-y-4 pt-8 border-t border-nordic-gray'):
                        with ui.element('div').classes('flex items-center justify-between text-sm'):
                            ui.label('Grøn strøm %').classes('text-gray-500')
                            ui.label('92%').classes('font-bold text-primary-dark')
                        with ui.element('div').classes('flex items-center justify-between text-sm'):
                            ui.label('Månedlig rank').classes('text-gray-500')
                            ui.label('#12 i Aarhus').classes('font-bold text-[#0d1c12]')
                    
                    # CTA Sidebar
                    ui.label('Se fuld historik').classes('w-full mt-10 bg-white border border-nordic-gray py-3 rounded-lg text-sm font-bold hover:bg-gray-50 transition-colors text-center block cursor-pointer')

        # Footer
        with ui.element('footer').classes('mt-20 pt-12 border-t border-nordic-gray text-center text-gray-400 text-sm pb-12'):
            ui.label('© 2024 VoltWise. Skabt med fokus på fremtidens energi.')

@ui.page('/')
def index():
    setup_head()
    # Adding Tailwind classes to the body
    ui.query('body').classes('bg-white text-[#0d1c12] m-0 p-0 font-["Manrope"]')
    ui.query('.q-page-container').classes('p-0 m-0')
    ui.query('.q-page').classes('min-h-screen')

    # Root layout wrapper
    with ui.element('div').classes('min-h-screen flex h-screen overflow-hidden w-full'):
        create_sidebar()
        create_main_content()

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title='VoltWise Action Dashboard')
