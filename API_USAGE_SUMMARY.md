# SARB AI API Usage Summary

This document explains how each AI API works and how it will be used in the SARB car sharing application.

## 1. التنبؤ بالطلب (AI Demand Forecasting)

### كيف يعمل النظام:
- يحلل بيانات الحجوزات السابقة (historical booking data)
- يدرس الأنماط الموسمية (seasonal trends)
- يتتبع سلوك المستخدمين (user behaviours)
- يتنبأ بالفترات ذات الطلب المرتفع وتأثير الأحداث والمواسم

### الـ API:
```
GET /api/ai/forecast-demand/{area_id}
```

### كيف سيتم استخدامه في التطبيق:
- **في خريطة التطبيق**: إظهار مناطق الطلب المرتفع بألوان مختلفة
- **في تقويم الحجز**: تسليط الضوء على الأيام ذات الطلب العالي
- **للإشعارات التلقائية**: إرسال تنبيهات لل_hosts_ عن الفترات المزدحمة
- **للتخطيط الاستراتيجي**: مساعدة فريق الإدارة على فهم أنماط الطلب

### مثال على الاستخدام:
```javascript
// في تطبيق الويب أو الهاتف
fetch('/api/ai/forecast-demand/1')
  .then(response => response.json())
  .then(data => {
    // تحديث الخريطة بالألوان حسب مستوى الطلب
    updateMapWithDemand(data.expected_demand);
    
    // عرض تنبيه للمستخدم إذا كان الطلب مرتفعًا
    if (data.expected_demand > 0.8) {
      showNotification("توقعات طلب مرتفعة في منطقتك!");
    }
  });
```

## 2. التسعير الذكي (AI Pricing Optimization)

### كيف يعمل النظام:
- يقارن السيارات المشابهة في نفس المنطقة
- يحلل أداء الحجوزات للسيارات الأخرى
- يأخذ في الاعتبار مستويات الطلب المتوقع
- يقترح أسعارًا مثالية لل_hosts_ لزيادة الأرباح

### الـ API:
```
GET /api/ai/recommend-price/{car_id}
```

### كيف سيتم استخدامه في التطبيق:
- **في لوحة تحكم المضيف**: عرض اقتراحات التسعير
- **أثناء تحديث الأسعار**: تقديم توصيات فورية عند تغيير الأسعار
- **لمقارنة السوق**: إظهار الفرق بين السعر الحالي ومتوسط السوق
- **للتحذيرات الذكية**: تنبيه_hosts_ إذا كان سعرهم غير تنافسي

### مثال على الاستخدام:
```javascript
// في صفحة إدارة السيارة للـ host
fetch('/api/ai/recommend-price/38')
  .then(response => response.json())
  .then(data => {
    // عرض التوصية في واجهة المستخدم
    document.getElementById('price-recommendation').innerHTML = `
      <p>السعر الحالي: ${data.current_price} ريال</p>
      <p>السعر المقترح: ${data.recommended_price} ريال</p>
      <p>السبب: ${data.reason}</p>
    `;
    
    // تمييز السعر المقترح إذا كان مختلفًا بشكل كبير
    if (Math.abs(data.recommended_price - data.current_price) > 100) {
      highlightPriceRecommendation();
    }
  });
```

## 3. الإشعارات الذكية (AI Notifications)

### كيف يعمل النظام:
- يرسل تنبيهات لل_hosts_ حول الفترات القادمة ذات الطلب العالي
- يشجع_hosts_ على جعل سياراتهم متاحة للحجز في تلك الفترات

### الـ API:
```
GET /api/ai/host-notifications/{host_id}
```

### كيف سيتم استخدامه في التطبيق:
- **الإشعارات الفورية**: إرسال تنبيهات عبر التطبيق والبريد الإلكتروني
- **في لوحة تحكم_hosts_**: عرض تنبيهات المواسم والفرص التجارية
- **للتخطيط المسبق**: مساعدة_hosts_ على التحضير لفترات الذروة
- **للتحفيز**: تشجيع_hosts_ على تحسين توفر سياراتهم

### مثال على الاستخدام:
```javascript
// في تطبيق الهاتف للـ host
fetch('/api/ai/host-notifications/15')
  .then(response => response.json())
  .then(data => {
    // عرض الإشعارات في قائمة الإشعارات
    data.demand_notifications.forEach(notification => {
      addNotificationToUI({
        type: 'demand',
        title: 'فرصة تجارية',
        message: notification.message,
        date: notification.date,
        action: 'Make cars available'
      });
    });
    
    // عرض التنبيهات الموسمية
    data.seasonal_notifications.forEach(notification => {
      addNotificationToUI({
        type: 'seasonal',
        title: notification.period,
        message: notification.message,
        action: notification.recommendation
      });
    });
  });
```

## 4. الخوارزمية 1 (Algorithm 1: Initial Pricing)

### كيف يعمل النظام:
- يوصي بسعر مبدئي عند إدراج سيارة جديدة
- يقارن السيارات المماثلة في نفس المنطقة
- يحلل معدلات الحجز الخاصة بها

### الـ API:
```
GET /api/ai/recommend-initial-price?car_type={type}&location={location}
```

### كيف سيتم استخدامه في التطبيق:
- **أثناء إضافة سيارة جديدة**: تقديم سعر افتراضي ذكي
- **في نموذج إدراج السيارة**: ترشيد عملية تحديد السعر لل_hosts_ الجدد
- **لمقارنة السوق**: إظهار الأسعار المماثلة في المنطقة
- **لتقليل الأخطاء**: منع_hosts_ الجدد من تحديد أسعار غير منطقية

### مثال على الاستخدام:
```javascript
// في نموذج إضافة سيارة جديدة
function suggestInitialPrice(carType, location) {
  fetch(`/api/ai/recommend-initial-price?car_type=${carType}&location=${location}`)
    .then(response => response.json())
    .then(data => {
      // ملء حقل السعر تلقائيًا بالقيمة المقترحة
      document.getElementById('daily-price').value = data.recommended_initial_price;
      
      // عرض معلومات المقارنة
      document.getElementById('pricing-info').innerHTML = `
        <p>متوسط السوق: ${data.market_average_price} ريال</p>
        <p>عدد السيارات المماثلة: ${data.similar_cars_count}</p>
        <p>السبب: ${data.reason}</p>
      `;
    });
}

// استدعاء الدالة عند اختيار نوع السيارة والموقع
document.getElementById('car-type').addEventListener('change', function() {
  const carType = this.value;
  const location = document.getElementById('location').value;
  suggestInitialPrice(carType, location);
});
```

## 5. الخوارزمية 2 (Algorithm 2: Cancellation Policy)

### كيف يعمل النظام:
- يطبق سياسة الإلغاء قبل 24 ساعة لضمان وضوح الشروط

### الـ API:
```
GET /api/ai/can-cancel/{booking_id}
```

### كيف سيتم استخدامه في التطبيق:
- **قبل إلغاء الحجز**: التحقق من صلاحية الإلغاء
- **في تفاصيل الحجز**: عرض حالة إمكانية الإلغاء
- **لمنع النزاعات**: ضمان وضوح شروط الإلغاء للجميع
- **لإدارة المخاطر**: تقليل الإلغاءات المفاجئة

### مثال على الاستخدام:
```javascript
// في صفحة تفاصيل الحجز للمستخدم
function checkCancellationEligibility(bookingId) {
  fetch(`/api/ai/can-cancel/${bookingId}`)
    .then(response => response.json())
    .then(data => {
      // تحديث واجهة المستخدم
      const cancelButton = document.getElementById('cancel-booking-btn');
      const cancellationInfo = document.getElementById('cancellation-info');
      
      if (data.can_cancel) {
        cancelButton.disabled = false;
        cancelButton.style.display = 'block';
        cancellationInfo.innerHTML = `
          <span class="success">يمكن إلغاء هذا الحجز</span>
          <p>${data.reason}</p>
        `;
      } else {
        cancelButton.disabled = true;
        cancellationInfo.innerHTML = `
          <span class="error">لا يمكن إلغاء هذا الحجز</span>
          <p>${data.reason}</p>
        `;
      }
    });
}

// استدعاء الدالة عند تحميل صفحة الحجز
window.addEventListener('load', function() {
  checkCancellationEligibility(currentBookingId);
});
```

## ملخص الاستخدام في التطبيق

### للـ Hosts:
1. **التسعير الذكي**: مساعدة في تحديد أسعار تنافسية
2. **التنبؤ بالطلب**: معرفة متى سيكون الطلب مرتفعًا
3. **الإشعارات الذكية**: تلقي تنبيهات عن الفرص التجارية
4. **التسعير الأولي**: الحصول على اقتراحات للأسعار عند إضافة سيارة جديدة

### للـ Guests:
1. **التوصيات الشخصية**: عرض السيارات الأنسب لاحتياجاتهم
2. **معلومات التسعير**: فهم لماذا تم تحديد سعر معين
3. **شروط واضحة**: معرفة متى يمكن إلغاء الحجز

### للإدارة:
1. **تحليل البيانات**: فهم أنماط الطلب والسلوك
2. **التخطيط الاستراتيجي**: اتخاذ قرارات مبنية على البيانات
3. **تحسين الخدمة**: تحسين تجربة المستخدم للجميع

## فوائد النظام:

### للمستخدمين:
- تجربة أكثر ذكاءً وملاءمة
- أسعار تنافسية ومنطقية
- شفافية في الشروط والسياسات

### للـ Hosts:
- زيادة الأرباح من خلال التسعير الأمثل
- زيادة فرص الحجز من خلال التوقيت المناسب
- دعم في اتخاذ القرارات التجارية

### للمنصة:
- تحسين كفاءة السوق
- زيادة رضا المستخدمين
- بناء نظام ذكي وقابل للتطوير