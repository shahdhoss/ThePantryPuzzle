import sqlite3

# connection = sqlite3.connect("D:\\SWE - project\\ThePantryPuzzle\\instance\\MainDB.db")
# cursor = connection.cursor()

# table_query = "alter table Recipes add Recipe_Image BLOB"
# drop_table = "alter table Recipes drop column Recipe_Image"
# new_table = """create table Recipe_Images(
#         Recipe_Name varchar(50),
#         Recipe_Image BLOB
# )"""
# cursor.execute(new_table)

# connection.commit()
# connection.close()


def convert_to_binary(filename):
    with open(filename, "rb") as file:
        blob_date = file.read()
    return blob_date

def insert_blob(recipe_name, image):
    try:
        connection = sqlite3.connect("D:\\SWE - project\\ThePantryPuzzle\\instance\\MainDB.db")
        cursor = connection.cursor()
        query = "insert into Recipe_Images values (?, ?)"
        recipe_img = convert_to_binary(image)
        cursor.execute(query, (recipe_name, recipe_img))
        connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("failed to insert blob data into sqlite table", error)
    finally:
        if connection:
            connection.close()

# meat
# insert_blob("Meat Stock","D:\\Downloads\\_083751ab-5c8d-487e-90cb-a744888fc5ba.jpg")
# insert_blob("Homemade Meat Broth","D:\\Downloads\\_0fe0ecde-e8c7-4db3-b63c-978bc089e235.jpg")
# insert_blob("Crab-Meat-Stuffed Sole","D:\\Downloads\\_2bc485b8-8014-415c-8975-d604bf9c9444.jpg")
# insert_blob("Turkey Meat Loaf","D:\\Downloads\\_aa32e02e-9a53-411f-ab13-d5cc979bb046.jpg")
# insert_blob("Meat Loaf With Bacon","D:\\Downloads\\_ba5bb728-939b-4705-b2dd-168079c5b3c5.jpg")
# insert_blob("Meat Lovers' Supreme Pizza recipes","D:\\Downloads\\_13d0d570-a46c-457d-afb1-73f98f090431.jpg")
# insert_blob("Meat Loaf","D:\\Downloads\\_e3fe9df0-3e06-46f6-b02c-23c40dd6cbe5.jpg")
# insert_blob("Harlem Meat Loaf","D:\\Downloads\\_8cf735da-2846-4f6a-8189-6738a08a76d3.jpg")
# insert_blob("Souvlaki - Meat on a Stick","D:\\Downloads\\_f27097a8-c94b-4d82-8579-53060ba1caff.jpg")
# insert_blob("Savory Crepes with Meat Filling","D:\\Downloads\\_5b02ecab-925e-4732-8d95-c62c7f157cef.jpg")
# insert_blob("Favorite Meat Loaf","D:\\Downloads\\_209d0b0e-2435-4eaa-831e-38ddec4e1404.jpg")
# insert_blob("Chicken Taco Meat Tacos","D:\\Downloads\\_2d490431-1484-4dbf-b508-624225befc9d.jpg")
# insert_blob("Meat Lovers' Supreme Pizza", "D:\\Downloads\\_64f7b007-be0e-47d4-b2d2-341fe30c5633.jpg")
# insert_blob("Willin Low’s Luncheon Meat Fries With Kaffir Mayo", "D:\\Downloads\\_8457087e-b59a-4497-ab6c-2ebe9f789cba.jpg")
# insert_blob("Curried Ground Meat or Keema Matar", "D:\\Downloads\\_9a6feb88-3117-4964-9545-7337bbd22200.jpg")
# insert_blob("Chipotle Meat Loaf", "D:\\Downloads\\_9bd81dfc-275e-488e-8a86-d857a1eb0781.jpg")
# insert_blob("Chicken (or Any Other Meat) Stock", "D:\\Downloads\\_1d271349-5cb1-4094-b35a-f1bf48a163fd.jpg")
# insert_blob("Crab Meat Salad", "D:\\Downloads\\_82c53faf-718d-483f-a94e-a42cfb1f49a8.jpg")
# insert_blob("The Best Meat Loaf", "D:\\Downloads\\_09fad049-4232-4b80-a3ed-1221c62c5866.jpg")
# insert_blob("Orange-Ginger Turkey Meat Loaf", "D:\\Downloads\\_ca924776-8b2e-4238-83df-139a7d1077a8.jpg")

# fish
# insert_blob("Deep Fried Fish Bones","D:\\Downloads\\_77767505-9228-4197-9641-74331fc783bf.jpg" )
# insert_blob("Burnt-Scallion Fish", "D:\\Downloads\\_b91cdbfd-cdeb-4569-8433-8f45c7b4e45d.jpg")
# insert_blob("Curry-Crusted Fish", "D:\\Downloads\\_a6d63ba2-f314-42b5-985e-bf6a08eded40.jpg")
# insert_blob("Homemade fish fingers", "D:\\Downloads\\_39ae43f0-2e72-4eaa-8b62-77c0286f9d84.jpg")
# insert_blob("Gefilte Fish", "D:\\Downloads\\_03a10afa-fcae-4ed2-9f46-82d9e830f1e3.jpg")
# insert_blob("Breaded Sicilian Fish", "D:\\Downloads\\_6405d56c-e7ff-437c-b385-d7b939282884.jpg")
# insert_blob("Fish Stock", "D:\\Downloads\\_b9db501d-d29b-4ccd-8ea7-f939e18a46d1.jpg")
# insert_blob("Fish Sticks", "D:\\Downloads\\_5b6b1ec4-4b18-4c87-9518-ae6a983b4945.jpg")
# insert_blob("Baked Fish from Iceland", "D:\\Downloads\\_d5a5a6f0-749e-43a5-b9a7-d5eb5cff6f6d.jpg")
# insert_blob("Fish Curry", "D:\\Downloads\\_9a988cd1-095d-41cf-a342-bbefe529e32e.jpg")
# insert_blob("Fried Rock Fish", "D:\\Downloads\\_029868f0-83f8-40a0-84fb-b1aed5a338b8.jpg")
# insert_blob("Fish in Coconut Sauce", "D:\\Downloads\\_197e535a-a80d-4dcc-b005-2fd571c19962.jpg")
# insert_blob("Moroccan Fish", "D:\\Downloads\\_1ed79955-2c13-47a2-9038-3f61ee1c475c.jpg")
# insert_blob("Cod Fish Cakes", "D:\\Downloads\\_4efe6d4e-6946-4315-97e3-5554b445db59.jpg")
# insert_blob("Creamy Fish & Mussel Soup", "D:\\Downloads\\_46100bcd-8ad0-4cfd-b346-735f1227cd71.jpg")
# insert_blob("Seared and Steamed Fish", "D:\\Downloads\\_b75e8fd2-29fb-4090-a74d-23d355d8a735.jpg")
# insert_blob("Fish Broth", "D:\\Downloads\\_b9db501d-d29b-4ccd-8ea7-f939e18a46d1.jpg")


# vegetables
# insert_blob("Glazed Vegetables", "D:\\Downloads\\_849ec3b5-e692-418a-999e-fbf065038baf.jpg")
# insert_blob("Roasted Baby Vegetables", "D:\\Downloads\\_fe21baa8-871c-4cb8-8670-b38a8f51d323.jpg")
# insert_blob("Roasted Spring Vegetables", "D:\\Downloads\\_367caa56-cc50-43f7-983d-a47beb8a9bda.jpg")
# insert_blob("Saucy chicken & vegetables", "D:\\Downloads\\_082f162c-8050-4d96-b404-017012f529c4.jpg")
# insert_blob("Roasted Vegetables", "D:\\Downloads\\_2bb3e545-3051-44ed-b9af-2038db34867b.jpg")
# insert_blob("Steamed Meat Bao with Preserved Vegetables", "D:\\Downloads\\_c9b5f839-139d-47fe-a4ae-b3b46247d2ba.jpg")
# insert_blob("Turkey Sandwich With Provolone And Pickled Vegetables", "D:\\Downloads\\_3d505bfd-13b2-46a7-b5fc-958725196945.jpg")
# insert_blob("Low-key Iridofu Or Scrambled Tofu With Vegetables recipes", "D:\\Downloads\\_1efd859b-894c-481d-8715-875eb27dd57e.jpg")
# insert_blob("Moo Shu Vegetables", "D:\\Downloads\\_cbf7be33-d0b8-4863-92de-8ef73a4771ee.jpg")
# insert_blob("Quick-Pickled Vegetables", "D:\\Downloads\\_d1cf196c-96df-4243-bbcd-440805a4d108.jpg")
# insert_blob("Penne Pasta With Vegetables", "D:\\Downloads\\_55eaa761-bcf1-4640-baf0-cbff1cf50c0c.jpg")
# insert_blob("Spinach Salad with Roasted Vegetables and Apricot recipes", "D:\\Downloads\\_f58fdcbf-b241-456a-9347-ac6c4e0bc8d8.jpg")
# insert_blob("Mediterranean Marinated Vegetables", "D:\\Downloads\\_408687c6-0b31-4d3a-a6b8-9c2ac51c3751.jpg")
# insert_blob("Warm Artichoke Dip with Vegetables", "D:\\Downloads\\_72029dae-0908-4d03-8ad3-fa5da6a41f3d.jpg")
# insert_blob("Giardiniera (Italian Pickled Vegetables)", "D:\\Downloads\\_ccbbab33-0619-409d-9c9e-0ce09b8811e2.jpg")
# insert_blob("Oven Roasted Vegetables", "D:\\Downloads\\_b91fed2e-849f-4ed9-9778-82a5d3b4dc0c.jpg")
# insert_blob("Nutty Orzo and Vegetables", "D:\\Downloads\\_ebce2f1f-f7da-42a8-97ce-5ba4a0fa1d3c.jpg")
# insert_blob("Baby Vegetables with Tarragon Nage", "D:\\Downloads\\_ee1c933a-8067-48e1-aa3f-856dd669af5b.jpg")
# insert_blob("Hearty Black Bean Stew With Winter Vegetables", "D:\\Downloads\\_778933b8-5cf1-4aaf-8a02-9decf119041e.jpg")
# insert_blob("Curried Root Vegetables", "D:\\Downloads\\_ea8e82c9-6d16-4492-b783-8514906f4792.jpg")

# chicken
# insert_blob("Chicken Vesuvio", "D:\\Downloads\\_8ec51788-9dce-4650-8492-9c756ae775bb.jpg")
# insert_blob("Chicken Paprikash", "D:\\Downloads\\_d3066a6a-b633-4aa8-aac2-729224d0dda9.jpg")
# insert_blob("Baked Chicken", "D:\\Downloads\\_f0cb941d-d8e5-4b99-8d41-effbfb570481.jpg")
# insert_blob("Catalan Chicken", "D:\\Downloads\\_3fb5d03b-9a1b-4738-b5f2-db08be2201a0.jpg")
# insert_blob("Chicken Stew", "D:\\Downloads\\_f1b61d85-d0c9-45b0-8617-94491b599f14.jpg")
# insert_blob("Persian Chicken", "D:\\Downloads\\_fb36bd1c-4e84-4ff1-bf67-59be518f2b3e.jpg")
# insert_blob("Kreplach (Chicken Dumplings)", "D:\\Downloads\\_69fea65b-8372-4b19-9ca4-8747de73bc78.jpg")
# insert_blob("Chicken cacciatore", "D:\\Downloads\\_51300c21-bbec-48a4-b08e-bc84f16deb62.jpg")
# insert_blob("Roast Chicken", "D:\\Downloads\\_3dccdea3-2703-4aa6-8142-f3a9e453f61b.jpg")
# insert_blob("Chicken Crêpes", "D:\\Downloads\\_c65f474b-5678-4734-97b4-1e9a51f9cde8.jpg")
# insert_blob("Smothered Chicken", "D:\\Downloads\\_5f7d5cde-b84d-4dec-98a0-f13d59b60549.jpg")
# insert_blob("Chicken Hash", "D:\\Downloads\\_873a2960-1962-4fa5-9b73-ca797f6e9068.jpg")
# insert_blob("Chicken Poofs", "D:\\Downloads\\_39c16ed5-aa87-4c95-a7cb-f1112ccba7b8.jpg")
# insert_blob("Chicken Feet Stock", "D:\\Downloads\\_376222c6-491d-4082-a4e4-ede808719cc2.jpg")
# insert_blob("Chicken Soup", "D:\\Downloads\\_61689bd2-cf5f-47b1-b77c-ba5d50d19bb6.jpg")
# insert_blob("Chicken Pie", "D:\\Downloads\\_1f18d58b-8e0c-4ab3-addc-1b40430bbfe0.jpg")
# insert_blob("Chicken Enchiladas", "D:\\Downloads\\_13d8db68-b2ee-4659-b1b6-258342ed4c4f.jpg")
# insert_blob("Citrus Roasted Chicken", "D:\\Downloads\\_30f50766-6194-4b06-a084-a2f8d51c3d6f.jpg")
# insert_blob("Margarita Chicken", "D:\\Downloads\\_65bc1501-632d-4ce7-8c39-477cf3669a47.jpg")
