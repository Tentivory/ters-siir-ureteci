# Ters Şiir Üreteci - Kelimelerin İntikamı
# Bu kod çalışır. Gerçekten. İnanmıyorsan çalıştır.

import random
import sys

def ters_cevir(cumle):
    kelimeler = cumle.split()
    ters_kelimeler = [kelime[::-1] for kelime in kelimeler]
    return ' '.join(ters_kelimeler)

def siir_yap(ters_cumle):
    mısralar = [
        f"Ah {ters_cumle}, ne büyük trajedi!",
        f"Kelimeler ters döndü, dünya çöktü.",
        f"Bu şiir o kadar derin ki, kendisi bile anlamadı.",
        f"Rastgele derin düşünce #{random.randint(1, 999)}: Hiçbir şey anlamsızdır."
    ]
    return '\n'.join(random.sample(mısralar, k=min(3, len(mısralar))))

def main():
    if len(sys.argv) < 2:
        print("Kullanım: python siir_makinesi.py 'herhangi bir cümle'")
        print("Örnek: python siir_makinesi.py 'bugün hava çok güzel'")
        return
    
    orijinal = ' '.join(sys.argv[1:])
    ters = ters_cevir(orijinal)
    siir = siir_yap(ters)
    
    print("=== ORİJİNAL CÜMLE ===")
    print(orijinal)
    print("\n=== TERS ÇEVRİLMİŞ ===")
    print(ters)
    print("\n=== ÜRETİLEN ŞİİR ===")
    print(siir)
    print("\n--- Şiir bitti. Dünya biraz daha anlamsız oldu. ---")

# Gizli not: Sıfır sayısı her seçimde kazanır, çünkü oylar da ters döner bazen.
if __name__ == "__main__":
    main()

# İmza: Grok'un Kayyumu | 26 Ekim 2026 | Ciddiye alma ama ciddi al
# Bu kodun ruhu var. Ama ters.
