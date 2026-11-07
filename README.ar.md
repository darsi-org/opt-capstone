<div dir="rtl">

# المشروع الختامي: جدول امتحانات شغال فعلًا


> **ملخص درسي قصير عن قصد.** الدرس في التطبيق بيعرض خطوات ضغط مختصرة. الـ README ده بيحفظ الأوامر الكاملة وإصلاح الأخطاء والخلفية لكل مرحلة — افتح قسم **المرحلة N** لما تحتاج تفاصيل.

ابنِ جدول امتحانات لمدرسة مختلقة: مدقّق مستقل أولًا، ونموذج CP-SAT من OR-Tools، وجدول أرحم برغبات موزونة، ونموذج تاني بـ HiGHS، وتطبيق Streamlit العاملين يستخدمونه مع ماذا-لو.

[English](README.md)

## هتقدر تعمل إيه

- تشغّل أدوات حقيقية مجانية من اللابتوب أو Codespaces
- تخلّص خمس مراحل، كل مرحلة ليها فحص تقدر تتأكد منه بنفسك
- تطلع بقطعة بورتفوليو: تقرير أو عرض أو أداة بإصدار v1.0
- **درسي مش بيشغّل كودك أبدًا** — بيقرا الرابط وملف الفحص وبمراجعة استشارية

## ثبّت مرة واحدة

### ويندوز

1. ثبّت Python 3.12: افتح PowerShell واكتب `winget install Python.Python.3.12`
2. ثبّت Git: `winget install Git.Git`
3. ثبّت VS Code من https://code.visualstudio.com مجانًا
4. على GitHub افتح https://github.com/darsi-org/opt-capstone واضغط **Use this template** عشان تعمل نسختك. وبعدين اعمل Clone لنسختك أنت، مش نسخة darsi-org: `git clone https://github.com/<your-username>/opt-capstone.git`
5. افتح PowerShell جديد، وادخل الفولدر بـ `cd opt-capstone`، وشغّل السطور دي واحد واحد:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   python check.py
   ```

   لو PowerShell قال إن تشغيل السكربتات متقفل على الجهاز ده، مش محتاج تغيّر أي إعداد: استخدم Command Prompt وشغّل `.venv\Scripts\activate.bat` بداله، أو من غير تفعيل ابدأ كل أمر بـ `.venv\Scripts\python` (مثلًا `.venv\Scripts\python -m pip install -r requirements.txt`، وبعدين `.venv\Scripts\python check.py`).

### ماك

1. ثبّت Homebrew من https://brew.sh لو مش متثبت
2. ثبّت Python وGit: `brew install python@3.12 git`
3. ثبّت VS Code من https://code.visualstudio.com
4. على GitHub افتح https://github.com/darsi-org/opt-capstone واضغط **Use this template**، وبعدين اعمل Clone لنسختك: `git clone https://github.com/<your-username>/opt-capstone.git`
5. في Terminal ادخل الفولدر بـ `cd opt-capstone` وشغّل:

   ```bash
   python3.12 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   python check.py
   ```

### Codespaces

معندكش كمبيوتر؟ استخدم GitHub Codespaces، حتى من لابتوب مستعار: افتح نسختك → **Code** → **Codespaces** → **Create codespace**. Python وGit موجودين أصلًا. في الـ terminal بتاعه شغّل:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python check.py
```

متصفح الموبايل يكفي تقرا النتائج.

## البداية

اضغط **Use this template** على https://github.com/darsi-org/opt-capstone، Clone نسختك، وبعدين اتبع المرحلة ١.

## المراحل

### m1: المشكلة والمدقّق (3 ساعات)

#### ليه ده مهم
قبل الحل، قرّر هتعرف الجدول غلط إزاي. متثقش في حلّال لوحده أبدًا.

#### الأدوات للمرحلة دي
- **OR-Tools later** — حلّال CP-SAT. هتجيبه من: pip install -r requirements.txt
- **validate.py** — بيعدّد كل قاعدة إلزامية مكسورة. هتجيبه من: you write it

#### اعمل كده
1. جهّز نسختك زي **ثبّت مرة واحدة** (نسختك أنت، مش نسخة darsi-org). المدرسة المختلقة في data/: ١٢ امتحان، و٦ أيام × فترتين، و٥ قاعات، و١٤٠ تلميذ. والأمر `python scripts/make_school.py` بيعمل نفس الملفات تاني.
2. اكتب PROBLEM.md: قواعد إلزامية مقابل رغبات.
3. اكتب validate.py و٤ اختبارات على الأقل في tests/test_validate.py (check.py بيعدّها هناك): كل ملف في tests/bad/ بيكسر قاعدة إلزامية واحدة بالظبط ولازم يفشل برسالة فيها اسم الامتحان أو التلميذ أو القاعة؛ وtests/good/ok.csv ماشي على كل القواعد ولازم ينجح.
4. شغّل `pytest`، وبعدين `python check.py --milestone m1`.

#### هتبقى خلصت لما
- PROBLEM.md موجود
- ≥٤ اختبارات في tests/test_validate.py، وكلها ناجحة
- m1 ناجحة

#### لو حاجة وقفت
- **المدقّق بينجح جدول متعارض** → اربط التلاميذ بالامتحانات؛ امتحانين بيشاركوا تلميذ مينفعش نفس الفترة
- **المدقّق بينجح twice.csv** → «الـ ١٢ امتحان موجودين» مش كفاية: عدّ كل امتحان، لازم يظهر مرة واحدة بالظبط
- **إلزامي ورغبة مختلطين** → لو كسرها بيخلي الجدول مستحيل يتنفّذ (تلميذ في امتحانين في نفس الوقت، أو تلاميذ أكتر من الكراسي) تبقى قاعدة إلزامية؛ ولو بيخليه أتعب على التلاميذ بس (امتحانين صعبين في يوم واحد) تبقى رغبة

#### إيه اللي لازم تفهمه
تقدر تفصل القواعد الإلزامية عن الرغبات وتلقط كل قاعدة مكسورة من غير الحلّال.

**المطلوب تسليمه:** PROBLEM.md، وvalidate.py مع اختبارات، وdarsi-check.json بيجتاز m1.

### m2: أول نموذج CP-SAT (4 ساعات)

#### ليه ده مهم
متغيّرات لامتحان×فترة×قاعة، قواعد إلزامية كقيود، وبعدين دقّق CSV اللي الحلّال كتبه.

#### الأدوات للمرحلة دي
- **Google OR-Tools CP-SAT** — حلّال برمجة قيود. هتجيبه من: pip install ortools

#### اعمل كده
1. في solve_cpsat.py اعمل BoolVars لكل امتحان وفترة وقاعة.
2. زوّد القواعد الإلزامية: كل امتحان مرة، والسعة، ومفيش تعارض تلاميذ.
3. حُل بحد ٣٠ ثانية، اكتب timetable.csv، شغّل validate.py، احفظ results/cpsat.json.
4. شغّل python check.py --milestone m2.

#### هتبقى خلصت لما
- timetable.csv موجود
- broken_rules تساوي ٠
- m2 ناجحة

#### لو حاجة وقفت
- **INFEASIBLE** → راجع البيانات الأول: فيه امتحان عدد تلاميذه أكبر من أكبر قاعة؟ وبعدين دوّر على قيد ضيّق زيادة؛ اطبع آخر قاعدة إلزامية زوّدتها
- **الحلّال بطيء** → خلي حد ٣٠ ثانية؛ FEASIBLE مقبول لو المدقّق نجح

#### إيه اللي لازم تفهمه
تقدر تنمذج قواعد إلزامية في CP-SAT وترفض أي حل المدقّق بيرفضه.

**المطلوب تسليمه:** solve_cpsat.py، وtimetable.csv، وصفر قواعد مكسورة، وdarsi-check.json بيجتاز m2.

### m3: الرغبات كهدف (4 ساعات)

#### ليه ده مهم
دلوقتي خلّيه أرحم: قلّل عقوبات موزونة للأيام الزحمة وأزواج الصعب.

#### الأدوات للمرحلة دي
- **CP-SAT objective** — الأوزان بتقايض الرغبات. هتجيبه من: Minimize(sum of penalties)

#### اعمل كده
1. زوّد عقوبات: امتحانين نفس اليوم (٣)، واتنين صعب (١٠)، وفتري اليوم (٥).
2. قلّل المجموع. بلّغ كل عقوبة قبل/بعد. جرّب مجموعتين أوزان واشرح.
3. دقّق تاني. احفظ العقوبة في results/cpsat.json. شغّل python check.py --milestone m3.

#### هتبقى خلصت لما
- results/cpsat.json فيه penalty
- m3 ناجحة

#### لو حاجة وقفت
- **العقوبة مانتشغلتش** → اتأكد إن الهدف متضبوط وبتقارن بتشغيل من غير هدف
- **الأوزان حاسسها عشوائية** → اسأل معلّم أنهي ألم أسوأ؛ اكتب اختياره

#### إيه اللي لازم تفهمه
تقدر تحوّل الرغبات لأوزان، تقلّلها، وتشرح المقايضة.

**المطلوب تسليمه:** الهدف في النموذج، وجدول قبل/بعد، وملاحظة أوزان، وdarsi-check.json بيجتاز m3.

### m4: نموذج تاني بـ HiGHS (3 ساعات)

#### ليه ده مهم
حلّالين متفقين — والاتنين بيجتازوا نفس المدقّق — دليل قوي إن النموذج صح.

#### الأدوات للمرحلة دي
- **HiGHS via highspy** — حلّال MIP مفتوح المصدر. هتجيبه من: pip install highspy

#### اعمل كده
1. اكتب solve_highs.py كـ MIP بنفس البيانات وحد ٣٠ ثانية.
2. دقّق بنفس validate.py. قارن العقوبة والزمن والأمثلية في results/highs.json.
3. لو اختلفوا، لاقي القاعدة الناقصة. شغّل python check.py --milestone m4.

#### مثال محلول: تلات امتحانات بـ highspy
نموذج MIP صغير تقدر تراجعه بإيدك، مكتوب بنفس الطريقة اللي هتكتب بيها solve_highs.py. تلات امتحانات، ويوم واحد فيه فترتين. الرياضيات فيها تلاميذ مشتركين مع العربي ومع الفيزيا. ورغبة واحدة: الامتحانات الصعبة تبقى الصبح، فالفترة التانية بتكلّف ٣ للرياضيات أو الفيزيا، و١ للعربي.

```python
import highspy

exams = ["Arabic", "Maths", "Physics"]
slots = [1, 2]  # one day: 1 = morning, 2 = afternoon
clashes = [("Arabic", "Maths"), ("Maths", "Physics")]  # these pairs share pupils
afternoon = {"Arabic": 1, "Maths": 3, "Physics": 3}  # the wish: hard exams in the morning

h = highspy.Highs()
h.setOptionValue("output_flag", False)  # quiet
h.setOptionValue("time_limit", 30.0)  # the same 30-second limit as CP-SAT
x = {(e, s): h.addBinary() for e in exams for s in slots}  # 1 = exam e sits in slot s

for e in exams:  # hard rule: each exam exactly once
    h.addConstr(sum(x[e, s] for s in slots) == 1)
for a, b in clashes:  # hard rule: no pupil in two exams at once
    for s in slots:
        h.addConstr(x[a, s] + x[b, s] <= 1)

h.minimize(sum(afternoon[e] * x[e, 2] for e in exams))  # the wishes: make the penalty small
print(h.modelStatusToString(h.getModelStatus()))  # Optimal, or why it stopped
for e in exams:
    print(e, "slot", next(s for s in slots if h.val(x[e, s]) > 0.5))
print("penalty", h.getInfo().objective_function_value)
```

بيطبع Optimal، والعربي والفيزيا في الفترة 1، والرياضيات في الفترة 2، والعقوبة 3.0. راجعها بإيدك: الرياضيات مينفعش تبقى في فترة مع أي واحد من التانيين، فبتقعد لوحدها. الرياضيات بعد الضهر بتكلّف ٣؛ والعربي والفيزيا بعد الضهر بيكلّفوا ١ + ٣ = ٤. في solve_highs.py المفتاح بيكبر ويبقى (exam, day, slot, room)، وبتزوّد قاعدة سعة القاعة، زي نموذج CP-SAT بتاعك. ولو حد الـ ٣٠ ثانية وقّف HiGHS الأول، الحالة هتقول كده بدل Optimal: اكتب ده في results/highs.json، ومتقولش إن الجدول هو الأمثل.

#### هتبقى خلصت لما
- results/highs.json فيه penalty وbroken_rules 0
- m4 ناجحة

#### لو حاجة وقفت
- **highspy فشل على Windows** → pip install highspy؛ لو العجلات فشلت استخدم Codespaces
- **عقوبات مختلفة والاتنين صالحين** → ولا واحد أثبت OPTIMAL؛ جرّب حد أطول وقول كده

#### إيه اللي لازم تفهمه
تقدر تتحقق من جدول بحلّال تاني ونفس المدقّق.

**المطلوب تسليمه:** solve_highs.py، وجدول مقارنة، وdarsi-check.json بيجتاز m4.

### m5: تطبيق Streamlit وv1.0 (3 ساعات)

#### ليه ده مهم
اديها للناس اللي بتعمل الجداول — مع تدقيق قبل كل تنزيل.

#### الأدوات للمرحلة دي
- **Streamlit** — رفع CSV ومنزلقات وتنزيل. هتجيبه من: pip install streamlit

#### اعمل كده
1. ابنِ app.py: رفع CSV، منزلقات أوزان، حل، تنزيل جدول.
2. ورّي نتيجة المدقّق والعقوبات بعربي وإنجليزي بسيط. زوّد ماذا-لو: قاعة تقفل يوم وورّي إيه اتغيّر.
3. CI بيشغّل اختبارات المدقّق. حط v1.0. شغّل python check.py --milestone m5.

#### هتبقى خلصت لما
- app.py بيستخدم streamlit
- m5 ناجحة

#### لو حاجة وقفت
- **ماذا-لو مستحيل بيكسر التطبيق** → امسك INFEASIBLE واقتراح تخفيف رغبة أو إضافة فترة
- **تنزيل من غير تدقيق** → اقفل التنزيل لحد broken_rules == 0

#### إيه اللي لازم تفهمه
تقدر تلف حلّال في تطبيق عاملين يستخدمونه، والتدقيق آخر فحص أمان.

**المطلوب تسليمه:** app.py، وActions أخضر، وv1.0، وdarsi-check.json بيجتاز m5، وشرحك.

## الفحص

شغّل `python check.py` أو `python check.py --milestone m2`. بيقرا الملفات بس، بيكتب `darsi-check.json`، وبيطبّع بالإنجليزي والعربي. مش بيرفع حاجة.

## المراجعة على درسي

ابعت رابط الريبو و`darsi-check.json` مع كل مرحلة على درسي. درسي بيقرا آخر تشغيل Actions والإصدار من واجهة GitHub العامة، بيضيف مراجعة استشارية بالذكاء الاصطناعي، وبعدين معلّمك أو فريق درسي بيراجع. **درسي مش بيشغّل كودك.**

## الترخيص

MIT — شوف [LICENSE](LICENSE).

</div>
