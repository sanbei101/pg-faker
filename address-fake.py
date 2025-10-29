from utils import set_and_sort, format_array_sql

provinces = [
    '上海市', '云南省', '北京市', '吉林省', '四川省', '天津市', '安徽省',
    '山东省', '山西省', '广东省', '江苏省', '江西省', '河北省', '河南省',
    '浙江省', '海南省', '湖北省', '湖南省', '甘肃省', '福建省', '贵州省',
    '辽宁省', '重庆市', '陕西省', '青海省', '黑龙江省', '西藏自治区',
    '内蒙古自治区', '宁夏回族自治区', '广西壮族自治区', '新疆维吾尔自治区'
]

cities = [
    '上海', '临汾', '丹东', '丽水', '乌海', '伊春', '保定', '六安', '包头',
    '北京', '南京', '南通', '台州', '合肥', '吉林', '吕梁', '唐山', '嘉兴',
    '四平', '大同', '大庆', '大连', '天津', '太原', '宁波', '安庆', '宿州',
    '宿迁', '常州', '廊坊', '徐州', '忻州', '扬州', '承德', '抚顺', '无锡',
    '晋中', '晋城', '朔州', '朝阳', '本溪', '杭州', '松原', '沈阳', '沧州',
    '泰州', '淮北', '淮南', '淮安', '温州', '湖州', '滁州', '白城', '白山',
    '盐城', '盘锦', '绍兴', '绥化', '舟山', '芜湖', '苏州', '营口', '蚌埠',
    '衡水', '衢州', '赤峰', '辽源', '辽阳', '运城', '通化', '通辽', '邢台',
    '邯郸', '重庆', '金华', '铁岭', '铜陵', '锦州', '镇江', '长春', '长治',
    '阜新', '阜阳', '阳泉', '鞍山', '鸡西', '鹤岗', '黄山', '黑河',
    '七台河', '佳木斯', '双鸭山', '哈尔滨', '张家口', '牡丹江', '石家庄',
    '秦皇岛', '葫芦岛', '连云港', '马鞍山', '乌兰察布', '呼伦贝尔', '呼和浩特',
    '巴彦淖尔', '鄂尔多斯', '齐齐哈尔'
]

street_prefixes = [
    '中华', '中山', '人民', '光明', '兴华', '前进', '友谊', '和平', '团结',
    '工农', '延安', '建设', '振兴', '文化', '新华', '朝阳', '民主', '民族',
    '红旗', '育才', '胜利', '解放', '长征', '青年'
]

street_suffixes = [
    '巷', '街', '路', '大街', '大道', '胡同'
]


streets = []
for prefix in street_prefixes:
    for suffix in street_suffixes:
        streets.append(f"{prefix}{suffix}")
neighborhood_prefixes = [
    '万科', '万达', '世纪', '世茂', '中信', '中海', '保利', '华润', '幸福',
    '恒大', '招商', '橡树', '碧水', '绿地', '绿城', '蓝湾', '融创', '远洋',
    '金地', '金色', '锦绣', '阳光', '雅居', '龙湖'
]

neighborhood_suffixes = [
    '城', '庭', '湾', '苑', '茂', '里', '公馆', '国际', '天地', '家园',
    '小区', '庄园', '新城', '江南', '绿洲', '花园', '幸福里', '雍华府', '中央广场',
    '城市花园', '春江彼岸', '香槟国际'
]

neighborhoods = []
for prefix in neighborhood_prefixes:
    for suffix in neighborhood_suffixes:
        neighborhoods.append(f"{prefix}{suffix}")
provinces = set_and_sort(provinces)
cities = set_and_sort(cities)
streets = set_and_sort(streets)
neighborhoods = set_and_sort(neighborhoods)

# 生成 SQL
sql = f"""-- fake中文地址(Python 自动生成)
CREATE OR REPLACE FUNCTION address_cn()
RETURNS TEXT AS $$
DECLARE
    provinces TEXT[] := {format_array_sql(provinces)};

    cities TEXT[] := {format_array_sql(cities)};

    streets TEXT[] := {format_array_sql(streets)};

    neighborhoods TEXT[] := {format_array_sql(neighborhoods)};

    province_count INT := array_length(provinces, 1);
    city_count INT := array_length(cities, 1);
    street_count INT := array_length(streets, 1);
    neighborhood_count INT := array_length(neighborhoods, 1);
    province TEXT;
    city TEXT;
    street TEXT;
    neighborhood TEXT;
BEGIN
    province := provinces[1 + floor(random() * province_count)::int];
    city := cities[1 + floor(random() * city_count)::int];
    street := streets[1 + floor(random() * street_count)::int];
    neighborhood := neighborhoods[1 + floor(random() * neighborhood_count)::int];
    RETURN province || city || neighborhood || street ||
           (10 + floor(random() * 90)::int)::text || '号';
END;
$$ LANGUAGE plpgsql;
"""

with open("dist/address-fake.sql", "w") as f:
    f.write(sql)