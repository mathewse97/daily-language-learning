# CHECKIN_LOG — histórico dos check-ins semanais

> **Fonte.** A artifact *Weekly Check-in* é onde Mathews responde; o planejador copia as
> notas para cá ao consumi-las (passo 8), e a partir daí este arquivo é o registro.
> A artifact é efêmera e se sobrescreve a cada semana; este arquivo não.
>
> Formato de uma linha: `data | GR | IT | EN | misses` — notas de 1 a 5, `misses` é a
> lista de itens não recordados, separada por vírgula, ou `—`.
> Escala em `OPERATIONS.md`.

```
FORMAT: data | gr | it | en | misses
2026-09-13 | 4 | 5 | 5 | —
```

Semanas sem linha são semanas sem check-in. O planejador aplica a regra conservadora
nesses casos e nunca preenche o que não recebeu.
