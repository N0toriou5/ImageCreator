# ImageCreator

**ImageCreator** è un progetto Python che utilizza modelli **Stable Diffusion** per generare immagini a partire da prompt testuali. Ottimizzato per **macOS con chip Apple Silicon (M1/M2/M3)**, sfrutta automaticamente **Metal Performance Shaders (MPS)** se disponibili, altrimenti ricade sull'uso della **CPU**.

---

## 🚀 Caratteristiche principali

* ✅ Supporta modelli Stable Diffusion locali
* ✍️ Prompt testuale semplice da CLI
* ⚙️ Compatibile con M1/M2/M3 (macOS >= 12.3)
* 🧠 Usa accelerazione Metal (GPU) se disponibile
* 🛡️ Fallback automatico su CPU
* 📦 Moduli principali: `diffusers`, `torch`, `transformers`

---

## 📦 Requisiti

* Python ≥ 3.9
* macOS ≥ 12.3
* Apple Silicon (M1/M2/M3)

### Installazione ambiente virtuale

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> ⚠️ Assicurati di usare una versione di `torch` compatibile con MPS su macOS. Per Apple Silicon, vedi la guida ufficiale: [https://pytorch.org](https://pytorch.org).

---

## 🧪 Esempio di utilizzo

```bash
python image_generator.py
```

Ti verrà chiesto di inserire un prompt, ad esempio:

```text
Un castello sospeso tra le nuvole al tramonto
```

L'immagine verrà generata nella directory di output specificata (default: `./outputs/`).

---

## ⚙️ Dettagli tecnici

* Il codice verifica la presenza di **MPS** (GPU Metal) con:

```python
torch.backends.mps.is_available()
```

* Se non disponibile, passa automaticamente a `torch.device("cpu")`

---

## 📁 Modello utilizzato

Assicurati di aver scaricato i file necessari (`unet`, `vae`, `text_encoder`, ecc.) del modello Stable Diffusion in una directory locale (`./realistic_vision` o simile).

> Se ottieni errori su file `.safetensors`, puoi usare `.bin` (PyTorch) ma **attenzione alla sicurezza** se il modello è stato scaricato da fonti non verificate.

---

## 🛠️ Troubleshooting

* ⚠️ **Errore NumPy 2.0**: Se ricevi errori con NumPy, prova a downgradare:

```bash
pip install "numpy<2"
```

* ⚠️ \*\*Torch \*\*\`\`: Alcune versioni recenti di `transformers` e `torch` richiedono aggiornamenti compatibili. Verifica le versioni consigliate in `requirements.txt`.

---

## 📃 Licenza

Questo progetto è distribuito sotto licenza MIT. Vedi il file `LICENSE` per maggiori dettagli.

---

## 🙏 Ringraziamenti

Basato su [Hugging Face Diffusers](https://github.com/huggingface/diffusers), [Transformers](https://github.com/huggingface/transformers) e [PyTorch](https://pytorch.org/).
