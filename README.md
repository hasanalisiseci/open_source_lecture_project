
# iOS Projelerinde Refaktörleme Commitlerinin Tespiti

Bu proje, iOS projelerindeki commit mesajlarını analiz ederek refaktörleme commitlerini tespit etmek amacıyla hazırlanmıştır. Çalışma, GitHub üzerindeki iOS projelerinden elde edilen verilerle gerçekleştirilmiş ve derin öğrenme modelleri kullanılarak commit mesajları otomatik olarak sınıflandırılmıştır.

## İçindekiler
1. [Proje Hakkında](#proje-hakkında)
2. [Gereksinimler](#gereksinimler)
3. [Kullanım](#kullanım)
4. [Kod Dosyaları](#kod-dosyaları)
5. [Dataset Hakkında](#dataset-hakkında)
6. [Çıktılar](#çıktılar)
7. [Bildiri](#bildiri)

---

## Proje Hakkında

Bu çalışmanın amacı, yazılım mühendisliği süreçlerinde kritik bir öneme sahip olan refaktörleme işlemlerini tespit ederek bu süreçleri otomatikleştirmektir. Çalışma kapsamında:
- GitHub üzerindeki beş popüler iOS projesinden commit mesajları toplanmıştır.
- Commit mesajları refaktörleme ile ilgili anahtar kelimeler temel alınarak etiketlenmiştir.
- XGBoost ve TF-IDF gibi teknikler kullanılarak bir derin öğrenme modeli eğitilmiştir.

---

## Gereksinimler

Projeyi çalıştırmadan önce aşağıdaki yazılımları ve kütüphaneleri kurmanız gerekmektedir:
- Python 3.7+
- Pandas
- NumPy
- scikit-learn
- XGBoost
- Matplotlib
- Seaborn
- GitPython (GitHub API'si için)

Kurulum için aşağıdaki komutu kullanabilirsiniz:

```bash
pip install pandas numpy scikit-learn xgboost matplotlib seaborn
```

---

## Kullanım

1. **Commit Verilerinin Çekilmesi:**
   - `pullgithubcommit.py` dosyasını çalıştırarak seçilen iOS projelerinin commit mesajlarını ve metadata bilgilerini çekebilirsiniz.

   ```bash
   python pullgithubcommit.py
   ```

2. **Refaktörleme Commitlerinin Analizi:**
   - `detectrefactorcolumn.py` dosyasını çalıştırarak çekilen commit mesajlarındaki refaktörleme ile ilgili commitleri tespit edin.

   ```bash
   python detectrefactorcolumn.py
   ```

3. **Derin Öğrenme Modelinin Eğitilmesi:**
   - `commit_dl.py` dosyasını kullanarak commit mesajları üzerinde derin öğrenme modeli ile sınıflandırma yapabilirsiniz.

   ```bash
   python commit_dl.py
   ```

---

## Kod Dosyaları

- **`pullgithubcommit.py`:** GitHub API'sini kullanarak projelerden commit mesajlarını ve metadata bilgilerini çeker. Veriler CSV formatında kaydedilir.
- **`detectrefactorcolumn.py`:** Commit mesajlarını refaktörleme ile ilgili anahtar kelimelere göre sınıflandırır ve bir sütun ekler.
- **`commit_dl.py`:** TF-IDF ve XGBoost modellerini kullanarak commit mesajlarını "refaktör" ve "refaktör değil" olarak sınıflandırır.

---

## Dataset Hakkında

Bu proje için kullanılan dataset, beş popüler iOS projesinden çekilen commit mesajlarını içermektedir. Örnek olarak aşağıdaki veri yapısı kullanılmıştır:

| SHA      | Author Name | Author Email      | Author Date         | Message             | Refactor |
|----------|-------------|-------------------|---------------------|---------------------|----------|
| abc12345 | John Doe    | john@example.com  | 2023-01-01 12:00:00 | refactor codebase   | True     |
| def67890 | Jane Smith  | jane@example.com  | 2023-01-02 15:00:00 | add new feature     | False    |

---

## Çıktılar

Modelin çıktıları:
- Doğruluk (Accuracy): %92.3
- F1-Score: %91.5
- Precision ve Recall değerleri, her bir proje bazında detaylı olarak raporlanmıştır.

Confusion Matrix ve performans raporları, `commit_dl.py` dosyasında otomatik olarak oluşturulmaktadır.

---

## Bildiri

Bu projeye ait bilimsel çalışma, **"Automated Detection of Refactoring Commits in iOS Repositories Using Deep Learning"** başlıklı bildiri olarak hazırlanmıştır. Bildiride:
- Veri toplama, işleme ve sınıflandırma süreçleri ayrıntılı olarak açıklanmıştır.
- Derin öğrenme modellerinin performansları değerlendirilmiştir.
- Çalışmanın yazılım mühendisliği süreçlerine katkıları vurgulanmıştır.

**Bildiri Dosyası:** [paper.pdf](./paper.pdf)

---

Bu proje hakkında geri bildirimlerinizi paylaşabilir veya katkıda bulunabilirsiniz. Keyifli çalışmalar! 😊
