from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Security(BaseModel):
    sid = models.IntegerField(default=0)
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    traded = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('-created', )
        verbose_name = 'Security'
        verbose_name_plural = 'Securities'
    
    def __str__(self):
        return f'{self.name} (self.sid)'
    
    @classmethod
    def create(cls,sid, symbol, name):
        return cls.objects.create(sid=sid, symbol=symbol, name=name)
    
    @classmethod
    def check_security_exists(cls, sid, symbol):
        return cls.objects.filter(sid=sid, symbol__iexact=symbol).exists()
    


class SecurityDetail(BaseModel):
    symbol = models.CharField(max_length=20, db_index=True, primary_key=True)
    sector = models.CharField(max_length=100)
    shares_outstanding = models.IntegerField(default=0)
    market_price = models.FloatField(default=0)
    percentage_change = models.FloatField(default=0)
    high = models.FloatField(default=0)
    low = models.FloatField(default=0)
    avg_180_day = models.FloatField(default=0)
    avg_120_day = models.FloatField(default=0)
    one_year_yield = models.FloatField(default=0)
    eps = models.FloatField(default=0)
    pe_ratio = models.FloatField(default=0)
    book_value = models.FloatField(default=0)
    pbv_value = models.FloatField(default=0)
    divident_percent = models.FloatField(default=0)
    bonus_percentage = models.FloatField(default=0)
    avg_30_day_volume = models.FloatField(default=0)
    market_capitalization = models.FloatField(default=0)

    class Meta:
        verbose_name = 'Security Detail'
        verbose_name = 'Securities Detail'
        ordering = ('symbol',)
    
    def __str__(self):
        return self.symbol
    
    @classmethod
    def check_symbol_exists(cls, symbol):
        return cls.objects.filter(symbol__iexact=symbol).exists()
    
    @classmethod
    def create(cls, record):
        high = 0
        low = 0
        
        if '-' in record['52_weeks_high_low']:
            high_low = record['52_weeks_high_low'].split('-')
            high = float(high_low[0])
            low = float(high_low[1])

        return cls.objects.create(
            symbol = record['symbol'],
            sector = record['sector'],
            shares_outstanding = record['shares_outstanding'],
            market_price = record['market_price'],
            percentage_change = record['percentage_change'],
            high=high,
            low=low,
            avg_180_day=record['180_day_average'],
            avg_120_day=record['120_day_average'],
            one_year_yield=record['1_year_yield'],
            eps=record['eps'],
            pe_ratio=record['pe_ratio'],
            book_value=record['book_value'],
            pbv_value=record['pbv'],
            divident_percent=record['percentage_dividend'],
            bonus_percentage=record['percentage_bonus'],
            avg_30_day_volume=record['30_day_avg_volume'],
            market_capitalization=record['market_capitalization']
        )

    @classmethod
    def update_symbol_info(cls, symbol, record):       
        detail_obj = cls.objects.filter(symbol__iexact=symbol).first()
        high=detail_obj.high
        low=detail_obj.low
        
        if '-' in record['52_weeks_high_low']:
            high_low = record['52_weeks_high_low'].split('-')
            high = float(high_low[0])
            low = float(high_low[1])
        
        detail_obj.shares_outstanding = record['shares_outstanding'],
        detail_obj.market_price = record['market_price'],
        detail_obj.percentage_change = record['percentage_change'],
        detail_obj.high=high
        detail_obj.low=low
        detail_obj.avg_180_day=record['180_day_average'],
        detail_obj.avg_120_day=record['120_day_average'],
        detail_obj.one_year_yield=record['1_year_yield'],
        detail_obj.eps=record['eps'],
        detail_obj.pe_ratio=record['pe_ratio'],
        detail_obj.divident_percent=record['percentage_dividend'],
        detail_obj.bonus_percentage=record['percentage_bonus'],
        detail_obj.avg_30_day_volume=record['30_day_avg_volume'],
        detail_obj.market_capitalization=record['market_capitalization']
        detail_obj.save()