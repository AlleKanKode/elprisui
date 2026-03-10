#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VoltWise Action Dashboard - NiceGUI Implementation
Korrigeret version med CSS inde i page-funktionen
"""

from nicegui import ui

# ============================================================================
# COMPONENT FUNCTIONS
# ============================================================================

def create_navigation():
    """Create the top navigation bar"""
    with ui.element('div').classes('dashboard-header'):
        # Logo
        with ui.element('div').classes('logo'):
            ui.icon('bolt').style('font-size: 1.5rem; color: white;')
            ui.label('VoltWise')
        
        # Navigation links
        with ui.element('div').classes('nav-links'):
            nav_items = [
                ('dashboard', 'Dashboard', True),
                ('history', 'Historik', False),
                ('devices', 'Enheder', False),
                ('person', 'Profil', False),
                ('settings', 'Indstillinger', False)
            ]
            for icon, label, active in nav_items:
                cls = 'nav-link active' if active else 'nav-link'
                with ui.element('a').classes(cls):
                    ui.icon(icon).style('font-size: 1rem;')
                    ui.label(label)


def create_status_banner():
    """Create the green power status banner"""
    with ui.element('div').classes('status-banner'):
        # Left side - status
        with ui.element('div').classes('status-left'):
            ui.icon('eco').style('color: #166534;')
            ui.label('Status: Grøn strøm netop nu')
        
        # Right side - price and refresh
        with ui.element('div').classes('status-right'):
            ui.label('Nuværende pris').style('font-size: 0.9rem;')
            ui.label('2,45 kr. pr. kWh').classes('price-display')
            ui.button(
                'Opdater pris',
                icon='refresh',
                on_click=lambda: ui.notify('Priser opdateret!', type='positive')
            ).classes('refresh-btn')


def create_smart_delay_section():
    """Create the Smart Delay device cards"""
    # Section header
    with ui.element('div').classes('section-title'):
        ui.label('Smart Delay')
        with ui.element('a').classes('view-all-link'):
            ui.label('Se alle enheder')
            ui.icon('arrow_forward').style('font-size: 1rem;')
    
    ui.label('Optimér dit forbrug og spar penge ved at vente.').classes('section-subtitle')
    
    # Device data
    devices = [
        {
            'icon': 'dishwasher',
            'name': 'Opvaskemaskine',
            'start_price': '4,50 kr.',
            'wait_price': '1,20 kr.',
            'savings': '3,30 kr.',
            'wait_time': '01:00'
        },
        {
            'icon': 'dry_cleaning',
            'name': 'Tørretumbler',
            'start_price': '6,20 kr.',
            'wait_price': '2,10 kr.',
            'savings': '4,10 kr.',
            'wait_time': '01:00'
        },
        {
            'icon': 'ev_station',
            'name': 'Elbil',
            'start_price': '45,00 kr.',
            'wait_price': '15,50 kr.',
            'savings': '29,50 kr.',
            'wait_time': '01:00'
        }
    ]
    
    # Create device cards
    for device in devices:
        with ui.card().classes('device-card'):
            # Device header
            with ui.element('div').classes('device-header'):
                ui.icon(device['icon']).classes('device-icon')
                ui.label(device['name'])
            
            # Pricing options
            with ui.element('div').classes('pricing-grid'):
                # Start now option
                with ui.element('div').classes('price-option'):
                    ui.label('Start nu').classes('price-label')
                    ui.label(device['start_price']).classes('price-value')
                
                # Wait option (highlighted)
                with ui.element('div').classes('price-option wait'):
                    ui.label('Vent og spar').classes('price-label')
                    ui.label(device['wait_price']).classes('price-value')
            
            # Savings badge
            ui.label(f"Spar {device['savings']}").classes('savings-badge')
            
            # Wait time
            with ui.element('div').classes('wait-time'):
                ui.icon('access_time').classes('wait-time-icon')
                ui.label(f"Vent til kl. {device['wait_time']}")


def create_share_section():
    """Create the social sharing section"""
    with ui.element('div').classes('share-section'):
        ui.icon('emoji_events').style('font-size: 1.5rem;')
        ui.label('Har du en god grøn stime?').classes('share-title')
        ui.label('Del dine resultater og inspirér andre til at spare.').classes('share-subtitle')
        ui.button(
            'Del min besparelse',
            icon='share',
            on_click=lambda: ui.notify('Link kopieret til udklipsholderen!', type='info')
        ).classes('share-btn')


def create_impact_section():
    """Create the impact/statistics section"""
    # Section header
    with ui.element('div').classes('section-title'):
        ui.icon('monitoring').style('margin-right: 0.5rem;')
        ui.label('Din Impact')
    
    # Impact cards grid
    with ui.element('div').classes('impact-grid'):
        # Lifetime savings card
        with ui.element('div').classes('impact-card'):
            ui.icon('savings').classes('impact-icon').style('color: var(--primary-color);')
            ui.label('Livstidsbesparelse').classes('impact-label')
            ui.label('1.245,50 kr.').classes('impact-value')
            ui.label('65% af dit månedlige mål nået').classes('impact-detail')
            with ui.element('div').classes('progress-bar'):
                ui.element('div').classes('progress-fill').style('width: 65%')
        
        # CO2 reduction card
        with ui.element('div').classes('impact-card'):
            ui.icon('eco').classes('impact-icon').style('color: var(--primary-color);')
            ui.label('CO2-reduktion').classes('impact-label')
            ui.label('342 kg.').classes('impact-value')
            ui.label('Svarer til at plante 14 træer 🌲').classes('impact-detail')
        
        # Green power percentage card
        with ui.element('div').classes('impact-card'):
            ui.icon('grid_on').classes('impact-icon').style('color: var(--primary-color);')
            ui.label('Grøn strøm %').classes('impact-label')
            ui.label('92%').classes('impact-value')
            ui.label('Månedlig rank').classes('impact-detail')
            ui.label('#12 i Aarhus').classes('rank-badge')
    
    # View history button
    with ui.element('div').classes('history-btn'):
        ui.button(
            'Se fuld historik',
            icon='history',
            on_click=lambda: ui.notify('Viser historik...', type='info'),
            color='secondary'
        )


def create_footer():
    """Create the page footer"""
    with ui.element('div').classes('footer'):
        ui.label('© 2024 VoltWise. Skabt med fokus på fremtidens energi.')


# ============================================================================
# MAIN PAGE - CSS MOVED INSIDE HERE
# ============================================================================

@ui.page('/')
def build_dashboard():
    """Main function to build the complete dashboard"""
    
    # ✅ CSS er nu INDE i page-funktionen (ikke i global scope)
    ui.add_head_html('''
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        
        :root {
            --primary-color: #10b981;
            --primary-dark: #059669;
            --secondary-color: #3b82f6;
            --background: #f8fafc;
            --surface: #ffffff;
            --text-primary: #1e293b;
            --text-secondary: #64748b;
            --border-color: #e2e8f0;
            --success-bg: #dcfce7;
            --success-text: #166534;
            --warning-bg: #fef3c7;
            --warning-text: #92400e;
            --purple-gradient-start: #6366f1;
            --purple-gradient-end: #8b5cf6;
        }
        
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            background: var(--background);
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            color: var(--text-primary);
            line-height: 1.5;
        }
        
        .dashboard-header {
            background: linear-gradient(135deg, var(--primary-color), var(--primary-dark));
            color: white;
            padding: 1rem 2rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .logo {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-weight: 700;
            font-size: 1.25rem;
        }
        
        .nav-links {
            display: flex;
            gap: 0.5rem;
        }
        
        .nav-link {
            color: rgba(255,255,255,0.9);
            text-decoration: none;
            padding: 0.5rem 1rem;
            border-radius: 0.5rem;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            gap: 0.25rem;
            font-size: 0.9rem;
            cursor: pointer;
        }
        
        .nav-link:hover, .nav-link.active {
            background: rgba(255,255,255,0.15);
            color: white;
        }
        
        .status-banner {
            background: var(--success-bg);
            color: var(--success-text);
            padding: 0.75rem 1.5rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid var(--border-color);
            font-size: 0.9rem;
        }
        
        .status-left, .status-right {
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        
        .price-display {
            font-weight: 600;
            font-size: 1.1rem;
        }
        
        .refresh-btn {
            background: var(--primary-color) !important;
            color: white !important;
            border: none !important;
            padding: 0.4rem 0.8rem !important;
            border-radius: 0.375rem !important;
            cursor: pointer !important;
            display: flex !important;
            align-items: center !important;
            gap: 0.25rem !important;
            font-size: 0.85rem !important;
            text-transform: none !important;
        }
        
        .section-title {
            font-size: 1.25rem;
            font-weight: 600;
            margin: 1.5rem 0 1rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        
        .section-subtitle {
            color: var(--text-secondary);
            font-size: 0.95rem;
            font-weight: 400;
            margin-bottom: 1rem;
        }
        
        .view-all-link {
            color: var(--primary-color);
            text-decoration: none;
            font-size: 0.9rem;
            display: flex;
            align-items: center;
            gap: 0.25rem;
            cursor: pointer;
        }
        
        .device-card {
            background: var(--surface);
            border-radius: 0.75rem;
            padding: 1rem;
            margin-bottom: 1rem;
            border: 1px solid var(--border-color);
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }
        
        .device-header {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            margin-bottom: 0.75rem;
            font-weight: 600;
            font-size: 1.1rem;
        }
        
        .device-icon {
            font-size: 1.5rem;
            color: var(--text-secondary);
        }
        
        .pricing-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 0.75rem;
            margin-bottom: 0.75rem;
        }
        
        .price-option {
            padding: 0.75rem;
            border-radius: 0.5rem;
            text-align: center;
            border: 2px solid var(--border-color);
            cursor: pointer;
            transition: all 0.2s;
        }
        
        .price-option:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        
        .price-option.wait {
            border-color: var(--primary-color);
            background: var(--success-bg);
        }
        
        .price-label {
            font-size: 0.8rem;
            color: var(--text-secondary);
            margin-bottom: 0.25rem;
        }
        
        .price-value {
            font-weight: 700;
            font-size: 1.1rem;
        }
        
        .savings-badge {
            background: var(--primary-color);
            color: white;
            padding: 0.25rem 0.75rem;
            border-radius: 1rem;
            font-size: 0.85rem;
            font-weight: 600;
            display: inline-block;
            margin: 0.5rem 0;
        }
        
        .wait-time {
            color: var(--text-secondary);
            font-size: 0.9rem;
            display: flex;
            align-items: center;
            gap: 0.25rem;
        }
        
        .wait-time-icon {
            font-size: 0.9rem;
            color: var(--text-secondary);
        }
        
        .share-section {
            background: linear-gradient(135deg, var(--purple-gradient-start), var(--purple-gradient-end));
            color: white;
            border-radius: 0.75rem;
            padding: 1.5rem;
            margin: 1.5rem 0;
            text-align: center;
        }
        
        .share-title {
            font-weight: 600;
            font-size: 1.1rem;
            margin: 0.5rem 0;
        }
        
        .share-subtitle {
            opacity: 0.9;
            font-size: 0.9rem;
            margin-bottom: 1rem;
        }
        
        .share-btn {
            background: white !important;
            color: var(--purple-gradient-start) !important;
            border: none !important;
            padding: 0.5rem 1.5rem !important;
            border-radius: 0.5rem !important;
            font-weight: 600 !important;
            cursor: pointer !important;
            display: inline-flex !important;
            align-items: center !important;
            gap: 0.25rem !important;
            text-transform: none !important;
        }
        
        .share-btn:hover {
            transform: scale(1.02);
        }
        
        .impact-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-top: 1rem;
        }
        
        .impact-card {
            background: var(--surface);
            border-radius: 0.75rem;
            padding: 1.25rem;
            border: 1px solid var(--border-color);
            text-align: center;
        }
        
        .impact-icon {
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
        }
        
        .impact-label {
            color: var(--text-secondary);
            font-size: 0.9rem;
            margin-bottom: 0.25rem;
        }
        
        .impact-value {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--primary-color);
            margin: 0.25rem 0;
        }
        
        .impact-detail {
            font-size: 0.8rem;
            color: var(--text-secondary);
        }
        
        .progress-bar {
            height: 0.5rem;
            background: var(--border-color);
            border-radius: 0.25rem;
            overflow: hidden;
            margin: 0.5rem 0;
        }
        
        .progress-fill {
            height: 100%;
            background: var(--primary-color);
            border-radius: 0.25rem;
            transition: width 0.3s ease;
        }
        
        .rank-badge {
            background: var(--warning-bg);
            color: var(--warning-text);
            padding: 0.25rem 0.5rem;
            border-radius: 0.375rem;
            font-size: 0.8rem;
            font-weight: 600;
            display: inline-block;
            margin-top: 0.5rem;
        }
        
        .history-btn {
            margin-top: 1.5rem;
            text-align: center;
        }
        
        .footer {
            text-align: center;
            padding: 2rem;
            color: var(--text-secondary);
            font-size: 0.85rem;
            border-top: 1px solid var(--border-color);
            margin-top: 2rem;
        }
    </style>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    ''')
    
    # Page title
    ui.page_title('VoltWise Action Dashboard')
    
    # Main container with max-width
    with ui.column().style('max-width: 800px; margin: 0 auto; padding: 0 1rem; width: 100%;'):
        create_navigation()
        create_status_banner()
        
        with ui.element('div').style('padding: 1rem 0;'):
            create_smart_delay_section()
            create_share_section()
            create_impact_section()
        
        create_footer()


# ============================================================================
# RUN APPLICATION
# ============================================================================

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(
        title='VoltWise Action Dashboard',
        favicon='⚡',
        port=8080,
        reload=True,
        dark=False,
        host='0.0.0.0'
    )