import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import time

class AlternativeInvestmentAnalyzer:
    def __init__(self):
        # Yahoo Finance üzerinden Altın (GC=F) ve Gümüş (SI=F) sembolleri
        self.assets = {
            'Altın': 'GC=F',
            'Gümüş': 'SI=F'
        }
        # Uyarı sistemi için eşik değerler (Örnek değerler)
        self.alert_thresholds = {
            'Altın': 2100.0, 
            'Gümüş': 24.0
        }

    def fetch_real_time_data(self):
        """Kıymetli metal fiyatlarını canlı API üzerinden çeker."""
        print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Canlı veriler çekiliyor...")
        current_prices = {}
        
        for name, symbol in self.assets.items():
            ticker = yf.Ticker(symbol)
            # Son 1 günlük veriyi alıp anlık fiyatı yakalıyoruz
            todays_data = ticker.history(period='1d')
            if not todays_data.empty:
                current_price = todays_data['Close'].iloc[-1]
                current_prices[name] = current_price
                print(f"Güncel {name} Fiyatı: ${current_price:.2f}")
                
        return current_prices

    def alert_system(self, current_prices):
        """Gerçek zamanlı veri akışında belirlenen eşikleri kontrol eder ve bildirim verir."""
        print("\n--- Bildirim Katmanı (Alerting System) ---")
        for name, price in current_prices.items():
            threshold = self.alert_thresholds[name]
            if price > threshold:
                print(f"🚨 ALARM: {name} fiyatı kritik eşiği ({threshold}) aştı! Anlık: ${price:.2f}")
            else:
                print(f"✅ {name} fiyatı normal seyrinde. (Eşik: ${threshold})")

    def visualize_investment_trends(self, period="1mo"):
        """Veri görselleştirme teknikleriyle son 1 aylık yatırım trendlerini analiz eder."""
        print(f"\nSon {period} trend analizi grafiği hazırlanıyor...")
        
        plt.figure(figsize=(12, 6))
        
        # Altın ve Gümüş için geçmiş verileri çek ve çiz
        for name, symbol in self.assets.items():
            ticker = yf.Ticker(symbol)
            hist_data = ticker.history(period=period)
            
            if name == 'Altın':
                color = '#FFD700' # Altın sarısı
            else:
                color = '#C0C0C0' # Gümüş rengi
                
            plt.plot(hist_data.index, hist_data['Close'], label=f'{name} Trendi', color=color, linewidth=2)

        plt.title('Kıymetli Metal (Altın/Gümüş) Fiyat Trend Analizi', fontsize=14)
        plt.xlabel('Tarih', fontsize=12)
        plt.ylabel('Fiyat (USD)', fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        # Grafiği kaydet ve göster
        plt.savefig('trend_analysis.png')
        print("Grafik 'trend_analysis.png' olarak kaydedildi ve ekranda gösteriliyor.")
        plt.show()

if __name__ == "__main__":
    # Sistemi Başlat
    analyzer = AlternativeInvestmentAnalyzer()
    
    # 1. Aşama: Veri Çekme
    live_prices = analyzer.fetch_real_time_data()
    
    # 2. Aşama: Anlık Bildirim Sistemi
    if live_prices:
        analyzer.alert_system(live_prices)
    
    # 3. Aşama: Veri Görselleştirme ve Analiz
    analyzer.visualize_investment_trends(period="1mo")