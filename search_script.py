import os
import re
from pathlib import Path
from sentence_transformers import SentenceTransformer, util

# 1. Load the model (Legal/Scientific text often benefits from 'all-MiniLM-L6-v2')
model = SentenceTransformer('all-MiniLM-L6-v2')

# 2. Official DSA Categories & Legal Seed Phrases
# Derived from EU 2022/2065 and Implementing Regulation 2024/2835
dsa_categories = {
    "Animal Welfare": [
        "Animal harm",
        "Unlawful sale of animals"
    ],
    "Conumer Information Infringements": [
        "Hidden adertisement or commerical communication, including by influencers",
        "Insufficient information on traders",
        "Misleading information about the characteristics of the goods and services",
        "Misleading information about the consumer's rights",
        "Non-compliance with pricing regulations"
    ],
    "Cyber Violence": [
        "Cyber bullying and intimidation",
        "Cyber harassment",
        "Cyber incitement to hatred or violence",
        "Cyber stalking",
        "Non-consensual (intimate) material sharing, including (image-based) sexual abuse (excluding content depicting minors)",
        "Non-consensual sharing of material containing deepfake or similar technology using a third party's features (excluding content depicting minors)"
    ],
    "Cyber Violence Against Women": [
        "Cyber bullying and intimidation against girls",
        "Cyber harassment against women",
        "Cyber stalking against women",
        "Gendered disinformation",
        "Illegal incitement to violence and hatred against women",
        "Non-consenual (intimate) material sharing against women, including (image-based) sexual abuse against women (excluding content depicting minors)",
        "Non-consensual sharing of material containing deepfake or similar technology using a third party's features against women (excluding content depicting minors)"
    ],
    "Data Protection and Privacy Violations": [
        "Biometric data breach",
        "Data falsification",
        "Missing processing ground for data",
        "Right to be forgotten"
    ],
    "Illegal or Harmful Speech": [
        "Defamation",
        "Discrimination",
        "Illegal incitement to violence and hatred based on protected characeteristics (hate speech)"
    ],
    "Intellectual Property Infringements": [
        "Copyright infringements",
        "Design infringements",
        "Geographical indications infringements",
        "Patent infringements",
        "Trade secret infringements",
        "Trademark infringements"
    ],
    "Negative effects on civic discourse or elections": [
        "Misinformation, disinformation, foreign information manipulation and interference",
        "Violation of EU law relevant to civic discourse or elections",
        "Violation of national law relevant to civic discourse or elections"
    ],
    "Protection of minors": [
        "Age-specific restrictions concerning minors",
        "Child sexual abuse material",
        "Child sexual abuse material containing deepfake or similar technology",
        "Grooming/sexual enticement of minors",
        "Unsafe challenges"
    ],
    "Risk for public security": [
        "Illegal organizations",
        "Risk for environmental damage",
        "Risk for public health",
        "Terrorist content"
    ],
    "Scams and/or fraud": [
        "Impersonation or account hijacking",
        "Inauthentic accounts",
        "Inauthentic listings",
        "Inauthentic user reviews",
        "Phishing",
        "Pyramid schemes"
    ],
    "Self-harm": [
        "Content promoting eating disorders",
        "Self-mutilation",
        "Suicide"
    ],
    "Unsafe, non-compliant or prohibited products": [
        "Prohibited or restricted products",
        "Unsafe or non-compliant products"
    ],
    "Violence": [
        "Coordinated harm",
        "General calls or incitement to violence and/or hatred",
        "Human exploitation",
        "Human trafficking",
        "Trafficking in women and girls"
    ],
    "Other violation of provider's terms and conditions": [
        "Adult sexual material",
        "Age-specific restrictions",
        "Geographical requirements",
        "Goods/services not permitted to be offered on the platform",
        "Language requirements",
        "Nudity"
    ],
    "Other": [
    "Type of illegal content not specificed by the public authority",
    "Type of illegal content not specificed by the notifier"
    ]
}

def semantic_search_dsa(directory_path, threshold=0.45):
    cat_names = list(dsa_categories.keys())
    # Combine phrases for each category into a single 'semantic concept'
    cat_seeds = [". ".join(phrases) for phrases in dsa_categories.values()]
    category_embeddings = model.encode(cat_seeds, convert_to_tensor=True)

    pathlist = Path(directory_path).rglob('*.md')

    for path in pathlist:
        if "README" in path.name: continue
        
        print(f"\n>>> ANALYZING: {path.parent.name} / {path.name}")
        
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Clean up Markdown (remove URLs/extra symbols) for better semantic focus
            clean_content = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', content)
            
            # Split into chunks (paragraphs or list items)
            chunks = [c.strip() for c in re.split(r'\n\n|\n\*|\n-', clean_content) if len(c.strip()) > 50]
            
            if not chunks: continue
            
            chunk_embeddings = model.encode(chunks, convert_to_tensor=True)
            cosine_scores = util.cos_sim(chunk_embeddings, category_embeddings)

            matches_found = 0
            for i, chunk in enumerate(chunks):
                # Find the best category match for this chunk
                best_cat_idx = cosine_scores[i].argmax().item()
                best_score = cosine_scores[i][best_cat_idx].item()

                if best_score >= threshold:
                    category = cat_names[best_cat_idx]
                    print(f"  [MATCH: {category}] Score: {best_score:.2f}")
                    print(f"  Text: {chunk[:200]}...")
                    print("-" * 30)
                    matches_found += 1
            
            if matches_found == 0:
                print("(No high-confidence matches found in this document)")

# Execute search on your EU data folder
semantic_search_dsa('./vlop-vlose-versions')