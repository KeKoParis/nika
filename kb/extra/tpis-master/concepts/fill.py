# Список названий понятий и их описания
concepts = {
    "nrel_ingredient_usage": {
        "description": "использование ингредиентов",
        "example": "Отношение связывает различные ингредиенты с их использованием в блюдах."
    },
    "nrel_cooking_time": {
        "description": "время приготовления",
        "example": "Отношение указывает на необходимое время для приготовления определенного блюда."
    },
    "nrel_cooking_method": {
        "description": "метод приготовления",
        "example": "Отношение описывает метод приготовления, используемый для конкретного блюда."
    },
    "nrel_meal_type": {
        "description": "тип приема пищи",
        "example": "Отношение связывает блюда с типом приема пищи, к которому они относятся (например, завтрак, обед, ужин)."
    },
    "nrel_nutritional_value": {
        "description": "питательная ценность",
        "example": "Отношение указывает на питательную ценность различных блюд."
    },
    "nrel_preparation_time": {
        "description": "время подготовки",
        "example": "Отношение описывает время, необходимое для подготовки ингредиентов перед приготовлением."
    },
    "nrel_cultural_significance": {
        "description": "культурное значение",
        "example": "Отношение связывает блюда с их культурным значением в разных странах."
    },
    "nrel_popularity": {
        "description": "популярность",
        "example": "Отношение указывает на популярность блюда в разных регионах."
    },
    "nrel_cooking_temperature": {
        "description": "температура приготовления",
        "example": "Отношение описывает температуру, необходимую для приготовления блюда."
    },
    "nrel_origin": {
        "description": "происхождение",
        "example": "Отношение связывает блюда с их географическим или культурным происхождением."
    }
}

# Шаблон для каждого понятия
content_template = """\
{concept}
<- sc_node_norole_relation;
<- relation;
<- binary_relation;
<- oriented_relation;
<- antireflexive_relation;
<- asymmetric_relation;
<- antitransitive_relation;
=> nrel_main_idtf:
   [{description}]
   (* <- lang_ru;; *);
=> nrel_first_domain: concept_first;
=> nrel_second_domain: concept_second;
=> nrel_definitional_domain:
   ...
   (*
      <= nrel_combination: {{
         concept_first;
         concept_second
      }};;
   *);
<- rrel_key_sc_element:
   ...
   (*
      => nrel_main_idtf:
       [Опр. ({description})]
       (* <- lang_ru;; *);
      <- definition;;
      <= nrel_sc_text_translation:
        ...
        (*
           -> rrel_example:
            [{description} - {example}]
            (* <- lang_ru;; *);;
        *);
      <= nrel_using_constants: {{
         concept_first;
         concept_second
      }};;
   *);
"""

# Создание файлов
for concept, details in concepts.items():
    # Имя файла
    filename = f"relations/{concept}.scs"
    
    # Заполнение контента
    content = content_template.format(concept=concept, description=details["description"], example=details["example"])
    
    # Запись в файл
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

print("Файлы успешно созданы с уникальным содержимым.")
