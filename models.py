from django.db import models

# Create marketplace dropdown choice  for Orders database
MARKETPLACE_CHOICE = (
    ("Amazon", "Amazon"),
    ("Walmart", "Walmart"),
    ("Ebay", "Ebay"),
    ("Zoro", "Zoro"),
    ("Magento", "Magento"),
    ("Wholesale", "Wholesale"),
    ("Others", "Others")
)


# Create your models here.
class GlobalProducts(models.Model):
    id = models.BigAutoField(primary_key=True)
    pfi_part_number = models.CharField(db_column='PFI_Part_Number', max_length=15, blank=True, null=True)
    item_title = models.CharField(db_column='Item_Title', max_length=500, blank=True, null=True)
    item_description = models.TextField(db_column='Item_Description', blank=True, null=True)
    item_abbreviated_description = models.CharField(db_column='Item_Abbreviated_Description', max_length=500,
                                                    blank=True, null=True)
    brand = models.CharField(db_column='Brand', max_length=100, blank=True, null=True)
    manufacturer = models.CharField(db_column='Manufacturer', max_length=100, blank=True, null=True)
    mfr_part_number = models.CharField(db_column='Mfr_Part_Number', max_length=100, blank=True, null=True)
    color = models.CharField(db_column='Color', max_length=100, blank=True, null=True)
    material = models.CharField(db_column='Material', max_length=100, blank=True, null=True)
    unit_of_measure = models.CharField(db_column='Unit_Of_Measure', max_length=100, blank=True, null=True)
    item_dimension_unit = models.CharField(db_column='Item_Dimension_Unit', max_length=100, blank=True, null=True)
    item_length = models.CharField(db_column='Item_Length', max_length=100, blank=True, null=True)
    item_width = models.CharField(db_column='Item_Width', max_length=100, blank=True, null=True)
    item_height = models.CharField(db_column='Item_Height', max_length=100, blank=True, null=True)
    item_weight = models.CharField(db_column='Item_Weight', max_length=100, blank=True, null=True)
    physical_dimensions = models.CharField(db_column='Physical_Dimensions', max_length=100, blank=True, null=True)
    item_package_qty = models.CharField(db_column='Item_Package_Qty', max_length=100, blank=True, null=True)
    item_lot_qty = models.CharField(db_column='Item_Lot_Qty', max_length=100, blank=True, null=True)
    published_price = models.CharField(db_column='Published_Price', max_length=100, blank=True, null=True)
    dealer_net_price = models.CharField(db_column='Dealer_Net_Price', max_length=200, blank=True, null=True)
    drop_stock = models.CharField(db_column='Drop_Stock', max_length=100, blank=True, null=True)
    country_of_origin = models.CharField(db_column='Country_of_Origin', max_length=100, blank=True, null=True)
    truck_parcel = models.CharField(db_column='Truck_Parcel', max_length=100, blank=True, null=True)
    fob_origin = models.CharField(db_column='Fob_Origin', max_length=100, blank=True, null=True)
    freight_class = models.CharField(db_column='Freight_Class', max_length=100, blank=True, null=True)
    unspsc = models.CharField(db_column='UNSPSC', max_length=100, blank=True, null=True)
    item_option_id = models.CharField(db_column='Item_Option_Id', max_length=100, blank=True, null=True)
    item_option_parameter = models.CharField(db_column='Item_Option_Parameter', max_length=100, blank=True, null=True)
    item_option_value = models.CharField(db_column='Item_Option_Value', max_length=100, blank=True, null=True)
    item_kit_indicator = models.CharField(db_column='Item_Kit_Indicator', max_length=100, blank=True, null=True)
    item_new_indicator = models.CharField(db_column='Item_New_Indicator', max_length=100, blank=True, null=True)
    item_sale_indicator = models.CharField(db_column='Item_Sale_Indicator', max_length=100, blank=True, null=True)
    item_clearance_indicator = models.CharField(db_column='Item_Clearance_Indicator', max_length=100, blank=True,
                                                null=True)
    special_handling_indicator = models.CharField(db_column='Special_Handling_Indicator', max_length=100, blank=True,
                                                  null=True)
    factory_quick_ship_indicator = models.CharField(db_column='Factory_Quick_Ship_Indicator', max_length=100,
                                                    blank=True, null=True)
    hazmat_indicator = models.CharField(db_column='Hazmat_Indicator', max_length=100, blank=True, null=True)
    features = models.CharField(db_column='Features', max_length=100, blank=True, null=True)
    bullet_name_1 = models.CharField(db_column='Bullet_Name_1', max_length=100, blank=True, null=True)
    bullet_value_1 = models.CharField(db_column='Bullet_Value_1', max_length=100, blank=True, null=True)
    bullet_name_2 = models.CharField(db_column='Bullet_Name_2', max_length=100, blank=True, null=True)
    bullet_value_2 = models.CharField(db_column='Bullet_Value_2', max_length=100, blank=True, null=True)
    bullet_name_3 = models.CharField(db_column='Bullet_Name_3', max_length=130, blank=True, null=True)
    bullet_value_3 = models.CharField(db_column='Bullet_Value_3', max_length=140, blank=True, null=True)
    bullet_name_4 = models.CharField(db_column='Bullet_Name_4', max_length=130, blank=True, null=True)
    bullet_value_4 = models.CharField(db_column='Bullet_Value_4', max_length=140, blank=True, null=True)
    bullet_name_5 = models.CharField(db_column='Bullet_Name_5', max_length=130, blank=True, null=True)
    bullet_value_5 = models.CharField(db_column='Bullet_Value_5', max_length=140, blank=True, null=True)
    equipment_group_classification = models.CharField(db_column='Equipment_Group_Classification', max_length=100,
                                                      blank=True, null=True)
    equipment_group_classification_level_1 = models.CharField(db_column='Equipment_Group_Classification_Level_1',
                                                              max_length=138, blank=True, null=True)
    equipment_group_classification_level_2 = models.CharField(db_column='Equipment_Group_Classification_Level_2',
                                                              max_length=138, blank=True, null=True)
    equipment_group_classification_level_3 = models.CharField(db_column='Equipment_Group_Classification_Level_3',
                                                              max_length=138, blank=True, null=True)
    image_main_url = models.CharField(db_column='Image_Main_URL', max_length=174, blank=True, null=True)
    image_small_url = models.CharField(db_column='Image_Small_URL', max_length=115, blank=True, null=True)
    image_thumbnail_url = models.CharField(db_column='Image_Thumbnail_URL', max_length=119, blank=True, null=True)
    image_text = models.CharField(db_column='Image_Text', max_length=184, blank=True, null=True)
    image_caption = models.CharField(db_column='Image_Caption', max_length=113, blank=True, null=True)
    image_main_name = models.CharField(db_column='Image_Main_Name', max_length=115, blank=True, null=True)
    upc_code = models.CharField(db_column='UPC Code', max_length=112, blank=True, null=True)
    pfi_part_number_new = models.CharField(db_column='PFI_Part_Number_New', max_length=119, blank=True, null=True)
    proposition65_key_ca = models.CharField(db_column='Proposition65_Key_CA', max_length=120, blank=True, null=True)
    flag_allow_free_freight = models.CharField(db_column='Flag_Allow_Free_Freight', max_length=123, blank=True,
                                               null=True)
    min_qty = models.CharField(db_column='Min_Qty', max_length=100, blank=True, null=True)
    flag_returnable = models.CharField(db_column='Flag_Returnable', max_length=115, blank=True, null=True)
    leadtime = models.DecimalField(db_column='Leadtime', max_digits=10, decimal_places=0, blank=True, null=True)
    map = models.CharField(db_column='Map', max_length=100, blank=True, null=True)
    ship_collect = models.CharField(db_column='Ship_collect', max_length=112, blank=True, null=True)
    state_restriction = models.CharField(db_column='State_restriction', max_length=117, blank=True, null=True)
    sales_qty_min = models.CharField(db_column='Sales_Qty_Min', max_length=113, blank=True, null=True)
    qty_available = models.CharField(db_column='Qty_available', max_length=113, blank=True, null=True)
    fixed_freight_price = models.CharField(db_column='Fixed_freight_price', max_length=119, blank=True, null=True)
    flag_cancellable = models.CharField(max_length=116, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    product_desc = models.TextField()
    product_specs = models.TextField()
    image_url = models.CharField(max_length=300)
    descriptive_name = models.CharField(max_length=500)
    sds_url = models.CharField(db_column='SDS_URL', max_length=170, blank=True, null=True)
    active = models.BooleanField(db_column='active', default=True)
    api_global_id = models.CharField(max_length=100, blank=True, null=True)
    api_price = models.FloatField(blank=True, null=True)
    api_stock = models.IntegerField(blank=True, null=True)
    api_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'global_products'


class TrueValueProducts(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_nbr = models.CharField(db_column='Item_Nbr', max_length=15, blank=True, null=True)
    srp_cost = models.DecimalField(db_column='Srp_Cost', decimal_places=2, max_digits=6, blank=True, null=True)
    member_cost = models.DecimalField(db_column='Member_Cost', decimal_places=2, max_digits=6, blank=True, null=True)
    ds_cost = models.DecimalField(db_column='Ds_Cost', decimal_places=2, max_digits=6, blank=True, null=True)
    # this is the cost for us. There are two other fields "srp_cost" and "ds_cost".
    short_description = models.CharField(db_column='Short_Description', max_length=100, blank=True, null=True)
    vendor_id = models.CharField(db_column='Vendor_Id', max_length=100, blank=True, null=True)
    dpt_code = models.CharField(db_column='Dpt_Code', max_length=100, blank=True, null=True)
    subclass_code = models.CharField(db_column='Subclass_Code', max_length=100, blank=True, null=True)
    vendor_name = models.CharField(db_column='Vendor_Name', max_length=100, blank=True, null=True)
    upc = models.CharField(db_column='UPC', max_length=100, blank=True, null=True)
    long_description = models.CharField(db_column='Long_Description', max_length=490, blank=True, null=True)
    weight = models.DecimalField(db_column='Weight', decimal_places=2, max_digits=6, blank=True, null=True)
    length = models.DecimalField(db_column='Length', decimal_places=2, max_digits=6, blank=True, null=True)
    width = models.DecimalField(db_column='Width', decimal_places=2, max_digits=6, blank=True, null=True)
    height = models.DecimalField(db_column='Height', decimal_places=2, max_digits=6, blank=True, null=True)
    pack_weight = models.DecimalField(db_column='Pack_Weight', decimal_places=2, max_digits=6, blank=True, null=True)
    pack_length = models.DecimalField(db_column='Pack_Length', decimal_places=2, max_digits=6, blank=True, null=True)
    pack_width = models.DecimalField(db_column='Pack_Width', decimal_places=2, max_digits=6, blank=True, null=True)
    pack_height = models.DecimalField(db_column='Pack_Height', decimal_places=2, max_digits=6, blank=True, null=True)
    retail_pack_qty = models.IntegerField(db_column='retail_pack_qty', blank=True, null=True)
    member_pack_qty = models.DecimalField(db_column='member_pack_qty', decimal_places=2, max_digits=6, blank=True,
                                          null=True)
    member_pack_type = models.CharField(db_column='member_pack_type', max_length=100, blank=True, null=True)
    member_break_pack = models.CharField(db_column='member_break_pack', max_length=100, blank=True, null=True)
    model = models.CharField(db_column='model', max_length=100, blank=True, null=True)
    item_picture_id = models.CharField(db_column='item_picture_id', max_length=100, blank=True, null=True)
    country_code = models.CharField(db_column='country_code', max_length=50, blank=True, null=True)
    to_be_discontinued = models.CharField(db_column='to_be_discontinued', max_length=50, blank=True, null=True)
    substitute_item_nbr = models.CharField(db_column='substitute_item_nbr', max_length=100, blank=True, null=True)
    retail_uom = models.CharField(db_column='retail_uom', max_length=100, blank=True, null=True)
    edit_divisor = models.CharField(db_column='Edit_Divisor', max_length=100, blank=True, null=True)
    exclusive_brand_code = models.CharField(db_column='Exclusive_Brand_Code', max_length=100, blank=True, null=True)
    Prop65Flag = models.CharField(db_column='Prop65Flag', max_length=100, blank=True, null=True)
    Prop65WarningText = models.CharField(db_column='Prop65WarningText', max_length=500, blank=True, null=True)
    MAPP = models.CharField(db_column='MAPP', max_length=10, blank=True, null=True)
    IMAPP = models.CharField(db_column='IMAPP', max_length=10, blank=True, null=True)
    OnlineRestriction = models.CharField(db_column='OnlineRestriction', max_length=100, blank=True, null=True)
    MAPPPrice = models.DecimalField(db_column='MAPPPrice', decimal_places=2, max_digits=10, blank=True, null=True)
    IMAPPPrice = models.DecimalField(db_column='IMAPPPrice', decimal_places=2, max_digits=10, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        verbose_name_plural = 'TrueValue products'  # this line to make the table name more readable.


class OrderInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    Order_ID = models.CharField(db_column='Order_ID', max_length=100, default="", blank=False)
    Vendor = models.CharField(db_column='Vendor', max_length=120, blank=True, null=True)

    class Meta:
        managed = True
        verbose_name_plural = 'Order Information'


class Orders(models.Model):
    id = models.BigAutoField(primary_key=True)
    Order_ID = models.CharField(db_column='Order_ID', max_length=100, default="", blank=False)
    # the marketplace will be rendered as dropdown
    Marketplace = models.CharField(db_column='Marketplace', choices=MARKETPLACE_CHOICE,
                                   max_length=100, blank=True, null=True)
    Order_Date = models.DateTimeField(db_column="Order_Date", blank=True, null=True)
    order_info = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, default="")

    # put vendor in the order information database
    # in the future, we may have multiple items in one order that need to be ordered from multiple vendors

    class Meta:
        managed = True
        verbose_name_plural = 'Orders'


class CategoriesMap(models.Model):
    id = models.BigAutoField(primary_key=True)
    level_4 = models.CharField(db_column='level_4', max_length=255, blank=True, null=True)
    level_3_magento = models.CharField(db_column='level_3_magento', max_length=255, blank=True, null=True)
    level_3 = models.CharField(db_column='level_3', max_length=255, blank=True, null=True)
    level_2_magento = models.CharField(db_column='level_2_magento', max_length=255, blank=True, null=True)
    level_2 = models.CharField(db_column='level_2', max_length=255, blank=True, null=True)
    level_1_magento = models.CharField(db_column='level_1_magento', max_length=255, blank=True, null=True)
    level_1 = models.CharField(db_column='level_1', max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'essendant_categories'


class Essedant(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    item_number = models.CharField(db_column='Item_Number', max_length=100, blank=True, null=True)
    item_stock_number_butted = models.CharField(db_column='Item_Stock_Number_Butted', max_length=100, blank=True,
                                                null=True)
    item_stock_numbr_unbutted = models.CharField(db_column='Item_Stock_Numbr_Unbutted', max_length=100, blank=True,
                                                 null=True)
    description_25_character = models.CharField(db_column='Description_25_Character', max_length=100, blank=True,
                                                null=True)
    description_125_character = models.TextField(db_column='Description_125_Character', blank=True, null=True)
    brand_long_name = models.CharField(db_column='Brand_Long_Name', max_length=100, blank=True, null=True)
    manufacturer_long_name = models.CharField(db_column='Manufacturer_Long_Name', max_length=100, blank=True, null=True)
    unit_of_measure = models.CharField(db_column='Unit_of_Measure', max_length=100, blank=True, null=True)
    list_price = models.CharField(db_column='List_Price', max_length=100, blank=True, null=True)
    cost_column_1_quantity_global_facility_glb_glb = models.CharField(
        db_column='Cost_Column_1_Quantity_GLOBAL_FACILITY_GLB_GLB', max_length=100, blank=True, null=True)
    cost_column_1_quantity_cranbury_cnj_50 = models.CharField(
        db_column='Cost_Column_1_Quantity_CRANBURY_CNJ_50', max_length=100, blank=True, null=True)
    cost_column_1_price_global_facility_glb_glb = models.CharField(
        db_column='Cost_Column_1_Price_GLOBAL_FACILITY_GLB_GLB', max_length=100, blank=True, null=True)
    cost_column_1_price_cranbury_cnj_50 = models.CharField(
        db_column='Cost_Column_1_Price_CRANBURY_CNJ_50', max_length=100, blank=True, null=True)
    cost_column_type_global_facility_glb_glb = models.CharField(
        db_column='Cost_Column_Type_GLOBAL_FACILITY_GLB_GLB', max_length=100, blank=True, null=True)
    cost_column_type_cranbury_cnj_50 = models.CharField(
        db_column='Cost_Column_Type_CRANBURY_CNJ_50', max_length=100, blank=True, null=True)
    active_indicator = models.CharField(db_column='Active_Indicator', max_length=100, blank=True, null=True)
    air_shippable_indicator = models.CharField(
        db_column='Air_Shippable_Indicator', max_length=100, blank=True, null=True)
    box_pack_quantity = models.CharField(db_column='Box_Pack_Quantity', max_length=100, blank=True, null=True)
    box_pack_unit = models.CharField(db_column='Box_Pack_Unit', max_length=100, blank=True, null=True)
    box_depth = models.CharField(db_column='Box_Depth', max_length=100, blank=True, null=True)
    box_height = models.CharField(db_column='Box Height', max_length=100, blank=True, null=True)
    box_width = models.CharField(db_column='Box Width', max_length=100, blank=True, null=True)
    box_expanded_weight = models.CharField(db_column='Box Expanded Weight', max_length=100, blank=True, null=True)
    carton_pack_quantity = models.CharField(db_column='Carton Pack Quantity', max_length=100, blank=True, null=True)
    carton_pack_unit = models.CharField(db_column='Carton Pack Unit', max_length=100, blank=True, null=True)
    carton_depth = models.CharField(db_column='Carton Depth', max_length=100, blank=True, null=True)
    carton_height = models.CharField(db_column='Carton Height', max_length=100, blank=True, null=True)
    carton_width = models.CharField(db_column='Carton Width', max_length=100, blank=True, null=True)
    carton_expanded_weight = models.CharField(db_column='Carton Expanded Weight', max_length=100, blank=True, null=True)
    carton_rounded_weight = models.CharField(db_column='Carton Rounded Weight', max_length=100, blank=True, null=True)
    consolidated_item_copy = models.TextField(db_column='Consolidated Item Copy', blank=True, null=True)
    country_of_origin_name = models.CharField(db_column='Country of Origin Name', max_length=100, blank=True, null=True)
    energy_star_rated_code = models.CharField(db_column='Energy Star Rated Code', max_length=100, blank=True, null=True)
    eo_number = models.CharField(db_column='EO Number', max_length=100, blank=True, null=True)
    epa_cpg_code = models.CharField(db_column='EPA CPG Code', max_length=100, blank=True, null=True)
    epa_list_n = models.CharField(db_column='EPA List N', max_length=100, blank=True, null=True)
    epa_number = models.CharField(db_column='EPA Number', max_length=100, blank=True, null=True)
    epa_registration = models.CharField(db_column='EPA Registration', max_length=100, blank=True, null=True)
    fda_certified = models.CharField(db_column='FDA Certified', max_length=100, blank=True, null=True)
    green_indicator = models.CharField(db_column='Green Indicator', max_length=100, blank=True, null=True)
    green_information = models.TextField(db_column='Green Information', blank=True, null=True)
    hazardous_material_code = models.CharField(db_column='Hazardous Material Code', max_length=100, blank=True,
                                               null=True)
    image_name_item = models.CharField(db_column='Image Name Item', max_length=100, blank=True, null=True)
    image_name_item_alt = models.TextField(db_column='Image Name Item Alt', blank=True, null=True)
    image_name_line_drawing = models.TextField(db_column='Image Name Line Drawing', blank=True, null=True)
    image_name_msds_pdf = models.CharField(db_column='Image Name MSDS PDF', max_length=100, blank=True, null=True)
    image_name_product_lit = models.CharField(db_column='Image Name Product Lit', max_length=100, blank=True, null=True)
    image_name_swatches = models.CharField(db_column='Image Name Swatches', max_length=100, blank=True, null=True)
    item_weight = models.CharField(db_column='Item Weight', max_length=100, blank=True, null=True)
    item_video_url = models.TextField(db_column='Item Video URL', blank=True, null=True)
    keywords = models.TextField(db_column='Keywords', blank=True, null=True)
    manufacturer_part_number = models.CharField(db_column='Manufacturer Part Number', max_length=100, blank=True,
                                                null=True)
    msds_code = models.CharField(db_column='MSDS Code', max_length=100, blank=True, null=True)
    national_stock_number = models.CharField(db_column='National Stock Number', max_length=100, blank=True, null=True)
    non_returnable_code = models.CharField(db_column='Non-Returnable Code', max_length=100, blank=True, null=True)
    package_includes = models.TextField(db_column='Package Includes', blank=True, null=True)
    product_class_code = models.CharField(db_column='Product Class Code', max_length=100, blank=True, null=True)
    product_class_description = models.TextField(
        db_column='Product Class Description', blank=True, null=True)
    product_class_cat_1_code = models.CharField(
        db_column='Product Class Cat 1 Code', max_length=100, blank=True, null=True)
    product_class_cat_1_desc = models.CharField(
        db_column='Product Class Cat 1 Desc', max_length=100, blank=True, null=True)
    product_class_cat_2_code = models.CharField(
        db_column='Product Class Cat 2 Code', max_length=100, blank=True, null=True)
    product_class_cat_2_desc = models.CharField(
        db_column='Product Class Cat 2 Desc', max_length=100, blank=True, null=True)
    product_class_cat_3_code = models.CharField(
        db_column='Product Class Cat 3 Code', max_length=100, blank=True, null=True)
    product_class_cat_3_desc = models.CharField(
        db_column='Product Class Cat 3 Desc', max_length=100, blank=True, null=True)
    product_class_cat_4_code = models.CharField(
        db_column='Product Class Cat 4 Code', max_length=100, blank=True, null=True)
    product_class_cat_4_desc = models.CharField(
        db_column='Product Class Cat 4 Desc', max_length=100, blank=True, null=True)
    product_number = models.CharField(db_column='Product Number', max_length=100, blank=True, null=True)
    prop_65_indicator = models.CharField(
        db_column='Prop 65 Indicator', max_length=100, blank=True, null=True)
    prop_65_label_indicator = models.CharField(
        db_column='Prop 65 Label Indicator', max_length=100, blank=True, null=True)
    prop_65_toxicity_chemical = models.TextField(
        db_column='Prop 65 Toxicity-Chemical', blank=True, null=True)
    prop_65_warning_message = models.TextField(
        db_column='Prop 65 Warning Message', blank=True, null=True)
    recycled_indicator = models.CharField(
        db_column='Recycled Indicator', max_length=100, blank=True, null=True)
    recycled_ctnt_pre_cons = models.CharField(
        db_column='Recycled Ctnt Pre-Cons', max_length=100, blank=True, null=True)
    recycled_ctnt_post_cons = models.CharField(
        db_column='Recycled Ctnt Post-Cons', max_length=100, blank=True, null=True)
    recycled_ctnt_total = models.CharField(
        db_column='Recycled Ctnt Total', max_length=100, blank=True, null=True)
    selling_copy_long = models.TextField(db_column='Selling Copy Long', blank=True, null=True)
    selling_point_1 = models.TextField(db_column='Selling Point #1', blank=True, null=True)
    selling_point_2 = models.TextField(db_column='Selling Point #2', blank=True, null=True)
    selling_point_3 = models.TextField(db_column='Selling Point #3', blank=True, null=True)
    selling_point_4 = models.TextField(db_column='Selling Point #4', blank=True, null=True)
    selling_point_5 = models.TextField(db_column='Selling Point #5', blank=True, null=True)
    selling_point_6 = models.TextField(db_column='Selling Point #6', blank=True, null=True)
    selling_point_7 = models.TextField(db_column='Selling Point #7', blank=True, null=True)
    selling_point_8 = models.TextField(db_column='Selling Point #8', blank=True, null=True)
    selling_point_9 = models.TextField(db_column='Selling Point #9', blank=True, null=True)
    selling_point_10 = models.TextField(db_column='Selling Point #10', blank=True, null=True)
    shipping_class_code = models.CharField(db_column='Shipping Class Code', max_length=100, blank=True, null=True)
    unspsc = models.CharField(db_column='UNSPSC', max_length=100, blank=True, null=True)
    upc_retail = models.CharField(db_column='UPC Retail', max_length=100, blank=True, null=True)
    upc_item_gtin = models.CharField(db_column='UPC Item GTIN', max_length=100, blank=True, null=True)
    ups_indicator = models.CharField(db_column='UPS Indicator', max_length=100, blank=True, null=True)
    price_plan_global_facility_glb_glb = models.CharField(
        db_column='Price Plan-GLOBAL FACILITY-GLB-GLB', max_length=100, blank=True, null=True)
    price_plan_cranbury_cnj_50 = models.CharField(
        db_column='Price Plan-CRANBURY-CNJ-50', max_length=100, blank=True, null=True)
    quantity = models.IntegerField(db_column='quantity', blank=True, null=True)
    category = models.ForeignKey(CategoriesMap, blank=True, null=True, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(db_column='active', default=True)

    class Meta:
        managed = True
        db_table = 'essedant'


class EssendantStateRestrictions(models.Model):
    id = models.BigAutoField(primary_key=True)
    pfx_num = models.CharField(db_column='PFX_NUM', max_length=255, blank=True, null=True)
    stk_num = models.CharField(db_column='STK_NUM', max_length=255, blank=True, null=True)
    st_cde = models.CharField(db_column='ST_CDE', max_length=255, blank=True, null=True)
    rstr_txt = models.CharField(db_column='RSTR_TXT', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'essendant_state_restrictions'


class UnspscFromCsv(models.Model):
    id = models.BigAutoField(primary_key=True)
    segment = models.CharField(max_length=255, blank=True, null=True)
    segment_title_en = models.CharField(db_column='segment-title_en', max_length=255, blank=True, null=True)
    segment_title_fr = models.CharField(db_column='segment-title_fr', max_length=255, blank=True, null=True)
    family = models.CharField(max_length=255, blank=True, null=True)
    family_title_en = models.CharField(db_column='family-title_en', max_length=255, blank=True, null=True)
    family_title_fr = models.CharField(db_column='family-title_fr', max_length=255, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=255, blank=True, null=True)
    class_title_en = models.CharField(db_column='class-title_en', max_length=255, blank=True, null=True)
    class_title_fr = models.CharField(db_column='class-title_fr', max_length=255, blank=True, null=True)
    commodity = models.CharField(max_length=255, blank=True, null=True)
    commodity_title_en = models.CharField(db_column='commodity-title_en', max_length=255, blank=True, null=True)
    commodity_title_fr = models.CharField(db_column='commodity-title_fr', max_length=255, blank=True, null=True)
    date_file_published = models.CharField(db_column='date-file-published', max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'unspsc_from_csv'


class ProdInventoryTracking(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_sku = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField(db_column='quantity', blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'prod_inventory_tracking'


class KrollProducts(models.Model):
    id = models.BigAutoField(primary_key=True)
    sku = models.CharField(db_column='SKU', max_length=255, blank=True, null=True)
    manufacturer=models.CharField(db_column='Manufacturer', max_length=255, blank=True, null=True)
    product_type_name = models.CharField(db_column='ProductTypeName', max_length=255, blank=True, null=True)
    parent_sku = models.CharField(db_column='ParentSKU', max_length=255, blank=True, null=True)
    product_name = models.CharField(db_column='ProductName', max_length=255, blank=True, null=True)
    list_price = models.CharField(db_column='ListPrice', max_length=255, blank=True, null=True)
    cost = models.CharField(db_column='Cost', max_length=255, blank=True, null=True)
    MAPPrice = models.CharField(db_column='MAPPrice', max_length=255, blank=True, null=True)
    upc_code = models.CharField(db_column='UPCCode', max_length=255, blank=True, null=True)
    manufacturer_part_number = models.CharField(db_column='ManufacturerPartNumber', max_length=255, blank=True, null=True)
    shipping_weight = models.CharField(db_column='ShippingWeight', max_length=255, blank=True, null=True)
    shipping_length = models.CharField(db_column='ShippingLength', max_length=255, blank=True, null=True)
    shipping_width = models.CharField(db_column='ShippingWidth', max_length=255, blank=True, null=True)
    shipping_height = models.CharField(db_column='ShippingHeight', max_length=255, blank=True, null=True)
    can_drop_ship = models.CharField(db_column='CanDropShip', max_length=255, blank=True, null=True)
    is_hazardous_material = models.CharField(db_column='IsHazardousMaterial', max_length=255, blank=True, null=True)
    restriction_agreement = models.CharField(db_column='RestrictionAgreement', max_length=255, blank=True, null=True)
    country_of_origin = models.CharField(db_column='CountryOfOrigin', max_length=255, blank=True, null=True)
    short_description = models.TextField(db_column='ShortDescription', blank=True, null=True)
    long_description = models.TextField(db_column='LongDescription', blank=True, null=True)
    image_file_small = models.CharField(db_column='ImageFileSmall', max_length=255, blank=True, null=True)
    small_image_alternative_text= models.CharField(db_column='SmallImageAlternateText', max_length=255, blank=True, null=True)
    image_file_medium= models.CharField(db_column='ImageFileMedium', max_length=255, blank=True, null=True)
    medium_image_alternate_text= models.CharField(db_column='MediumImageAlternateText', max_length=255, blank=True, null=True)
    qty_on_hand = models.CharField(db_column='QuantityOnHand', max_length=255, blank=True, null=True)
    active = models.BooleanField(db_column='active', default=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        managed = True
        db_table = 'Kroll_import'


class MagentoProducts(models.Model):
    id = models.BigAutoField(primary_key=True)
    prod_id = models.CharField(db_column="prod_id", max_length=100, blank=True, null=True)
    magento_sku = models.CharField(db_column='magento_sku', max_length=100, blank=True, null=True)
    global_product = models.ForeignKey(GlobalProducts, blank=True, null=True, on_delete=models.CASCADE)
    supplier = models.CharField(db_column="supplier", max_length=100, blank=True, null=True)
    tv_product = models.ForeignKey(TrueValueProducts, blank=True, null=True, on_delete=models.CASCADE)
    essendant_product = models.ForeignKey(Essedant, blank=True, null=True, on_delete=models.CASCADE)
    kroll_product = models.ForeignKey(KrollProducts, blank=True, null=True, on_delete=models.CASCADE)
    qty = models.CharField(db_column='qty', max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'magento_products'


class ZoroProducts(models.Model):
    id = models.IntegerField(primary_key=True)
    zoro_sku = models.CharField(max_length=255)
    vendor_sku = models.CharField(max_length=255, blank=True, null=True)
    vendor_id = models.CharField(max_length=255, blank=True, null=True)
    buy_supply_sku = models.CharField(max_length=255, blank=True, null=True)
    web_title = models.TextField(db_column='web_title', blank=True, null=True)
    price_to_zoro = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_stock = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'zoro_products'


class EssendantCost(models.Model):
    id = models.BigAutoField(primary_key=True)
    ess_item_num = models.CharField(db_column='Ess_Item_Num', max_length=100, blank=True, null=True)
    cost = models.DecimalField(db_column='Cost', decimal_places=2, max_digits=7, blank=True, null=True)
    cost_item = models.ForeignKey(Essedant, blank=True, null=True, on_delete=models.CASCADE)
    
    class Meta:
        managed = True
        db_table = 'essendant_cost'


class OakleyProducts(models.Model):
    id = models.BigAutoField(primary_key=True)
    sku = models.CharField(db_column='SKU', max_length=100, blank=True, null=True)
    product_title = models.CharField(db_column='Product_Title', max_length=255, blank=True, null=True)
    list_price = models.DecimalField(db_column='List_Price', decimal_places=2, max_digits=7, blank=True, null=True)
    acq_cost = models.DecimalField(db_column='ACQ_Cost', decimal_places=2, max_digits=7, blank=True, null=True)
    MAPPrice = models.DecimalField(db_column='MAPPrice', decimal_places=2, max_digits=7, blank=True, null=True)
    lens_width = models.IntegerField(db_column='Lens_Width', blank=True, null=True)
    lens_height = models.IntegerField(db_column='Lens_Height', blank=True, null=True)
    bridge_width = models.IntegerField(db_column='Bridge_Width', blank=True, null=True)
    temple_length = models.IntegerField(db_column='Temple_Length', blank=True, null=True)
    total_frame_width = models.IntegerField(db_column='Total_Frame_Width', blank=True, null=True)
    model = models.CharField(db_column='Model', max_length=50, blank=True, null=True)
    frame_color = models.CharField(db_column='Frame_Color', max_length=50, blank=True, null=True)
    lens_color = models.CharField(db_column='Lens_Color', max_length=50, blank=True, null=True)
    polarized=models.CharField(db_column='Polarized', max_length=10, blank=True, null=True)
    lens_technology=models.CharField(db_column='Lens_Technology', max_length=100, blank=True, null=True)
    frame_material=models.CharField(db_column='Frame_Material', max_length=100, blank=True, null=True)
    lens_material=models.CharField(db_column='Lens_Material', max_length=100, blank=True, null=True)
    upc_code = models.CharField(db_column='UPC_Code', max_length=255, blank=True, null=True)
    short_description = models.TextField(db_column='Short_Description', blank=True, null=True)
    long_description = models.TextField(db_column='Long_Description', blank=True, null=True)
    image_url= models.CharField(db_column='Image_URL', max_length=255, blank=True, null=True)
    category_1=models.CharField(db_column='Category_1', max_length=100, blank=True, null=True)
    category_2=models.CharField(db_column='Category_2', max_length=100, blank=True, null=True)
    category_3=models.CharField(db_column='Category_3', max_length=100, blank=True, null=True)
    active = models.BooleanField(db_column='active', default=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'oakley_products' 


class R3Products(models.Model):
    id = models.BigAutoField(primary_key=True)
    sku_number=models.CharField(db_column='SKU_Number', max_length=100, blank=True, null=True)
    mfr_number=models.CharField(db_column='Mfr_Number', max_length=100, blank=True, null=True)
    product_header= models.CharField(db_column='Product_header', max_length=200, blank=True, null=True)
    acq_price = models.DecimalField(db_column='ACQ_Price', decimal_places=2, max_digits=7, blank=True, null=True)
    MAPPrice = models.DecimalField(db_column='MAPPrice', decimal_places=2, max_digits=7, blank=True, null=True)
    upc_number = models.CharField(db_column='UPC_Number', max_length=200, blank=True, null=True)
    vendor_name=models.CharField(db_column='Vendor_Name', max_length=200, blank=True, null=True)
    vendor_number=models.CharField(db_column='Vendor_Number', max_length=200, blank=True, null=True)
    long_description=models.TextField(db_column='Long_Description', blank=True, null=True)
    uom=models.CharField(db_column='UOM', max_length=10, blank=True, null=True)
    qty_uom=models.CharField(db_column='Qty_UOM', max_length=10, blank=True, null=True)
    buy_multiple=models.IntegerField(db_column='Buy_Multiple', blank=True, null=True)
    buy_minimum=models.IntegerField(db_column='Buy_Minimum', blank=True, null=True)
    unit_sq_ft=models.CharField(db_column='Unit_Sq_Ft', max_length=100, blank=True, null=True)
    unit_weight_lbs=models.CharField(db_column='Unit_Weight_Lbs', max_length=100, blank=True, null=True)
    table_attribute_1=models.CharField(db_column='Table_Attribute_1', max_length=250, blank=True, null=True)
    table_attribute_2=models.CharField(db_column='Table_Attribute_2', max_length=250, blank=True, null=True)
    table_attribute_3=models.CharField(db_column='Table_Attribute_3', max_length=250, blank=True, null=True)
    table_attribute_4=models.CharField(db_column='Table_Attribute_4', max_length=250, blank=True, null=True)
    low_res_img_1=models.CharField(db_column='Low_Res_Img_1', max_length=250, blank=True, null=True)
    low_res_img_2=models.CharField(db_column='Low_Res_Img_2', max_length=250, blank=True, null=True)
    low_res_img_3=models.CharField(db_column='Low_Res_Img_3', max_length=250, blank=True, null=True)
    low_res_img_4=models.CharField(db_column='Low_Res_Img_4', max_length=250, blank=True, null=True)
    high_res_img_1=models.CharField(db_column='High_Res_Img_1', max_length=500, blank=True, null=True)
    high_res_img_2=models.CharField(db_column='High_Res_Img_2', max_length=250, blank=True, null=True)
    high_res_img_3=models.CharField(db_column='High_Res_Img_3', max_length=250, blank=True, null=True)
    high_res_img_4=models.CharField(db_column='High_Res_Img_4', max_length=250, blank=True, null=True)
    prop_65_warning=models.CharField(db_column='Prop_65_Warning', max_length=300, blank=True, null=True)
    hazard_material_code=models.CharField(db_column='Hazardous_Material_Code', max_length=100, blank=True, null=True)
    material_safety_data_sheet=models.CharField(db_column='Material_Safety_Data_Sheet', max_length=100, blank=True, null=True)
    category=models.CharField(db_column='Category', max_length=100, blank=True, null=True)
    subcategory=models.CharField(db_column='Subcategory', max_length=100, blank=True, null=True)
    section_subhead=models.CharField(db_column='Section_Subhead', max_length=100, blank=True, null=True)
    on_hand_500=models.IntegerField(db_column='On_Hand_500', blank=True, null=True)
    on_hand_502=models.IntegerField(db_column='On_Hand_502', blank=True, null=True)
    on_hand_503=models.IntegerField(db_column='On_Hand_503', blank=True, null=True)
    total_oh=models.IntegerField(db_column='Total_OH', blank=True, null=True)
    stock=models.BooleanField(db_column='Stock',  default=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'r3_products' 


class TrueValCats(models.Model):
    id = models.IntegerField(primary_key=True)
    mfg = models.CharField(db_column='MFG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255, blank=True, null=True)  # Field name made lowercase.
    c1 = models.CharField(db_column='C1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    c1new = models.CharField(db_column='C1New', max_length=255, blank=True, null=True)  # Field name made lowercase.
    c2 = models.CharField(db_column='C2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    c2new = models.CharField(db_column='C2new', max_length=255, blank=True, null=True)  # Field name made lowercase.
    c3 = models.CharField(db_column='C3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    c3new = models.CharField(db_column='C3NEW', max_length=255, blank=True, null=True)  # Field name made lowercase.
    c4new = models.CharField(db_column='C4NEW', max_length=255, blank=True, null=True)  # Field name made lowercase.
    unspsc = models.CharField(db_column='UNSPSC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    f11 = models.CharField(max_length=255, blank=True, null=True)
    f12 = models.CharField(max_length=255, blank=True, null=True)
    f13 = models.CharField(max_length=255, blank=True, null=True)
    f14 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'true_val_cats'


class TrueValProds(models.Model):
    id = models.IntegerField(primary_key=True)
    item_nbr = models.CharField(max_length=255, blank=True, null=True)
    srp_cost = models.FloatField(blank=True, null=True)
    member_cost = models.FloatField(blank=True, null=True)
    ds_cost = models.FloatField(blank=True, null=True)
    short_description = models.CharField(max_length=255, blank=True, null=True)
    vendor_id = models.CharField(max_length=255, blank=True, null=True)
    dpt_code = models.CharField(max_length=255, blank=True, null=True)
    class_code = models.CharField(max_length=255, blank=True, null=True)
    subclass_code = models.CharField(max_length=255, blank=True, null=True)
    vendor_name = models.CharField(max_length=255, blank=True, null=True)
    upc = models.CharField(max_length=255, blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    pack_weight = models.FloatField(blank=True, null=True)
    pack_length = models.FloatField(blank=True, null=True)
    pack_width = models.FloatField(blank=True, null=True)
    pack_height = models.FloatField(blank=True, null=True)
    retail_pack_qty = models.IntegerField(blank=True, null=True)
    member_pack_qty = models.IntegerField(blank=True, null=True)
    member_pack_type = models.CharField(max_length=255, blank=True, null=True)
    member_break_pack = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    item_picture_id = models.CharField(max_length=255, blank=True, null=True)
    country_code = models.CharField(max_length=255, blank=True, null=True)
    to_be_discontinued = models.CharField(max_length=255, blank=True, null=True)
    substitute_item_nbr = models.CharField(max_length=255, blank=True, null=True)
    retail_uom = models.CharField(max_length=255, blank=True, null=True)
    edit_divisor = models.IntegerField(db_column='Edit_Divisor', blank=True, null=True)
    exclusive_brand_code = models.CharField(db_column='Exclusive_Brand_Code', max_length=255, blank=True, null=True)
    prop65flag = models.CharField(db_column='Prop65Flag', max_length=255, blank=True, null=True)
    prop65warningtext = models.TextField(db_column='Prop65WarningText', blank=True, null=True)
    mapp = models.FloatField(db_column='MAPP', blank=True, null=True)
    imapp = models.FloatField(db_column='IMAPP', blank=True, null=True)
    onlinerestriction = models.CharField(db_column='OnlineRestriction', max_length=255, blank=True, null=True)
    mappprice = models.FloatField(db_column='MAPPPrice', blank=True, null=True)
    imappprice = models.FloatField(db_column='IMAPPPrice', blank=True, null=True)
    category = models.ForeignKey(TrueValCats, models.DO_NOTHING, blank=True, null=True)
    inventory = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'true_val_prods'
