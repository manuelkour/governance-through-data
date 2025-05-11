import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

font_path = '/usr/local/share/fonts/simhei.ttf'
font_prop = fm.FontProperties(fname=font_path)
fm.fontManager.addfont(font_path)

plt.rcParams['font.family'] = font_prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

data = {
        'AD': ['Beijing (北京)', 'Chongqing (重庆)', 'Shanghai (上海)', 'Tianjin (天津)', 
               'Guangxi (广西)', 'Inner Mongolia (内蒙古)', 'Ningxia (宁夏)', 'Xinjiang (新疆)', 
               'Tibet (西藏)', 'Anhui (安徽)', 'Fujian (福建)', 'Gansu (甘肃)', 'Guangdong (广东)',
               'Guizhou (贵州)', 'Hainan (海南)', 'Hebei (河北)', 'Heilongjiang (黑龙江)',
               'Henan (河南)', 'Hubei (湖北)', 'Hunan (湖南)', 'Jiangsu (江苏)', 'Jiangxi (江西)',
               'Jilin (吉林)', 'Liaoning (辽宁)', 'Qinghai (青海)', 'Shaanxi (陕西)',
               'Shandong (山东)', 'Shanxi (山西)', 'Sichuan (四川)', 'Yunnan (云南)',
               'Zhejiang (浙江)', 'PLA (中国人民解放军)'],
        'Blacklists_2025': [1, 0, 2, 8, None, 5, 2, 3, 2, 9, None, 4, 7, None, 1, 5, 5, 3, 1, None, 1, 0, 2, 1, None, 2, 4, 4, 1, 4, 6, None],
        'Redlists_2025': [1, 0, 1, 3, None, 5, 1, 1, 0, 2, None, 1, 5, None, 1, 2, 1, 0, 1, None, 2, 0, 1, 0, None, 4, 4, 2, 1, 1, 4, None],
        'Blacklists_2023': [1, 6, 5, 8, 3, 5, 4, 4, 3, 5, 8, 8, 8, 0, 2, 6, 6, 6, 4, 1, 6, 4, 2, 1, 0, 3, 11, 37, 3, 6, 3, None],
        'Redlists_2023': [1, 6, 1, 3, 2, 5, 4, 1, 1, 3, 6, 2, 9, 0, 2, 2, 2, 6, 1, 1, 7, 3, 1, 1, 0, 6, 6, 7, 1, 4, 4, None],
        'Blacklists_2019': [14, None, 11, 11, 7, 1, 1, 2, 15, 5, 11, 1, 19, 1, 2, 1, 3, 14, 8, 21, 5, 10, 16, 6, 22, 4, 15, 35, 3, 5, 11, 1],
        'Redlists_2019': [24, None, 2, 11, 7, 1, 1, 1, 15, 3, 6, 1, 14, 1, 1, 1, 3, 4, 3, 12, 4, 10, 1, 3, 5, 7, 7, 8, 1, 3, 3, 1]
    }

def create_difference_plot(prev_year, curr_year):
    df = pd.DataFrame(data)
    
    df = df.dropna(subset=[f'Blacklists_{prev_year}', f'Blacklists_{curr_year}', f'Redlists_{prev_year}', f'Redlists_{curr_year}'])
    
    df['Blacklists_Diff'] = df[f'Blacklists_{curr_year}'] - df[f'Blacklists_{prev_year}']
    df['Redlists_Diff'] = df[f'Redlists_{curr_year}'] - df[f'Redlists_{prev_year}']
    
    df = df.iloc[::-1].reset_index(drop=True)
    
    fig, ax = plt.subplots(figsize=(12, 16))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    
    y_pos = np.arange(len(df)) * 1.2
    
    bar_height = 0.35
    bar_spacing = 0.4
    
    shadow_offset = 0.05
    shadow_alpha = 0.2
    for i, (black_val, red_val) in enumerate(zip(df['Blacklists_Diff'], df['Redlists_Diff'])):
        ax.barh(y_pos[i] + bar_spacing/2 - shadow_offset, black_val, 
                height=bar_height, color='gray', alpha=shadow_alpha, zorder=1)
        ax.barh(y_pos[i] - bar_spacing/2 - shadow_offset, red_val, 
                height=bar_height, color='gray', alpha=shadow_alpha, zorder=1)
    
    black_grad = plt.cm.Greys(np.linspace(0.5, 0.9, 2))
    red_grad = plt.cm.Reds(np.linspace(0.5, 0.9, 2))
    
    blacklist_bars = ax.barh(y_pos + bar_spacing/2, df['Blacklists_Diff'], 
                            height=bar_height, color=black_grad[1], 
                            alpha=0.85, label='Blacklists', zorder=3,
                            edgecolor='black', linewidth=0.5)
    redlist_bars = ax.barh(y_pos - bar_spacing/2, df['Redlists_Diff'], 
                          height=bar_height, color=red_grad[1], 
                          alpha=0.85, label='Redlists', zorder=3,
                          edgecolor='darkred', linewidth=0.5)
    
    def add_labels(bars, values):
        for bar, val in zip(bars, values):
            width = val
            x_pos = width + 0.5 if width >= 0 else width - 0.5
            if width == 0:
                x_pos = 0.5
            
            label = f"+{int(width)}" if width > 0 else f"{int(width)}"
            if width == 0:
                label = "0"
            
            bar_center = bar.get_y() + bar.get_height()/2 - 0.025
            
            ax.text(x_pos, bar_center,
                   label,
                   va='center',
                   ha='left' if width >= 0 else 'right',
                   fontsize=9,
                   fontweight='bold',
                   color='#444444')
    
    add_labels(blacklist_bars, df['Blacklists_Diff'])
    add_labels(redlist_bars, df['Redlists_Diff'])
    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(df['AD'], fontsize=10)
    
    ax.axvline(x=0, color='#666666', linewidth=1.2, zorder=1)
    
    ax.set_title(f'Difference in # of Lists ({prev_year} - {curr_year})',
                pad=20, fontsize=12, fontweight='bold')
    ax.set_xlabel('Difference in # of Lists', fontsize=10)
    ax.set_ylabel('Administrative Division', fontsize=10)
    
    ax.legend(loc='upper right', frameon=True, framealpha=0.9,
             fontsize=9, bbox_to_anchor=(1.0, 1.0))
    
    ax.grid(axis='x', linestyle='--', alpha=0.15, zorder=0)
    
    max_abs_value = max(
        abs(df['Blacklists_Diff'].max()),
        abs(df['Blacklists_Diff'].min()),
        abs(df['Redlists_Diff'].max()),
        abs(df['Redlists_Diff'].min())
    )
    ax.set_xlim(-(max_abs_value + 5), max_abs_value + 5)
    
    for spine in ax.spines.values():
        spine.set_color('#444444')
        spine.set_linewidth(1.2)
    
    plt.subplots_adjust(left=0.25)
    
    plt.savefig(f'list_differences_{prev_year}_{curr_year}.png',
                dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()

def create_yearly_comparison():    
    df = pd.DataFrame(data)
    
    columns_to_check = ['Blacklists_2019', 'Blacklists_2023', 'Blacklists_2025',
                       'Redlists_2019', 'Redlists_2023', 'Redlists_2025']
    df = df.dropna(subset=columns_to_check)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 20), height_ratios=[1, 1])
    fig.patch.set_facecolor('white')
    
    bar_width = 0.25
    r1 = np.arange(len(df))
    r2 = [x + bar_width for x in r1]
    r3 = [x + bar_width for x in r2]
    
    black_grad = plt.cm.Greys(np.linspace(0.4, 0.8, 3))
    red_grad = plt.cm.Reds(np.linspace(0.4, 0.8, 3))
    
    shadow_offset = 0.05
    shadow_alpha = 0.2
    
    for i, (r, year) in enumerate(zip([r1, r2, r3], [2019, 2023, 2025])):
        ax1.bar(r, df[f'Blacklists_{year}'], width=bar_width, 
                color='gray', alpha=shadow_alpha, zorder=1)
        ax1.bar(r, df[f'Blacklists_{year}'], width=bar_width,
                color=black_grad[i], alpha=0.85, label=str(year),
                edgecolor='black', linewidth=0.8, zorder=3)
    
    for i, (r, year) in enumerate(zip([r1, r2, r3], [2019, 2023, 2025])):
        ax2.bar(r, df[f'Redlists_{year}'], width=bar_width,
                color='gray', alpha=shadow_alpha, zorder=1)
        ax2.bar(r, df[f'Redlists_{year}'], width=bar_width,
                color=red_grad[i], alpha=0.85, label=str(year),
                edgecolor='darkred', linewidth=0.8, zorder=3)
    
    for ax, title in [(ax1, 'Blacklists by Year'), (ax2, 'Redlists by Year')]:
        ax.set_xlabel('Administrative Division', fontsize=12, labelpad=10, fontproperties=font_prop)
        ax.set_ylabel('Number of Lists', fontsize=12, labelpad=10, fontproperties=font_prop)
        ax.set_title(title, pad=20, fontsize=14, fontweight='bold', fontproperties=font_prop)
        
        ax.set_xticks([r + bar_width for r in range(len(df))])
        ax.set_xticklabels(df['AD'], rotation=45, ha='right', fontproperties=font_prop)
        
        ax.legend(loc='upper right', frameon=True, framealpha=0.9,
                 fontsize=9, bbox_to_anchor=(1.0, 1.0))
        
        ax.grid(axis='y', linestyle='--', alpha=0.3, zorder=0)
        
        for spine in ax.spines.values():
            spine.set_color('#444444')
            spine.set_linewidth(1.2)
        
        ax.set_facecolor('white')
    
    plt.tight_layout()
    
    plt.savefig('yearly_comparison.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()

if __name__ == "__main__":    
    create_difference_plot(2023, 2025)
    create_difference_plot(2019, 2025)
    create_yearly_comparison()