import os
import zipfile

# Define the directory structure and file contents
sitemap = {
    "mgh-website": {
        "package.json": "{}",
        "pnpm-lock.yaml": "{}",
        "tsconfig.json": "{}",
        "hydrogen.config.ts": "{}",
        "shopify.config.ts": "{}",
        ".gitignore": "*\nnode_modules\n.DS_Store",
        "README.md": "# My Guy Worldwide",
        "src": {
            "components": {
                "global": {
                    "Layout.tsx": """
import React from 'react';
import { Seo } from '@shopify/hydrogen';
import Header from './Header';
import Footer from './Footer';
import styles from './Layout.module.css';

interface LayoutProps {
  children: React.ReactNode;
  title?: string;
}

export default function Layout({ children, title }: LayoutProps) {
  return (
    <div className={styles.container}>
      <Seo type="defaultSeo" data={{ title }} />
      <Header />
      <main className={styles.main}>{children}</main>
      <Footer />
    </div>
  );
}
                    """,
                    "Header.tsx": """
import React from 'react';
import { Link } from '@shopify/hydrogen';
import styles from './Header.module.css';

export default function Header() {
  return (
    <header className={styles.header}>
      <div className={styles.container}>
        <Link to="/" className={styles.logo}>MGH</Link>
        <nav className={styles.nav}>
          <Link to="/experiences" className={styles.navItem}>Experiences</Link>
          <Link to="/destinations" className={styles.navItem}>Destinations</Link>
          <Link to="/about" className={styles.navItem}>About Us</Link>
          <Link to="/contact" className={styles.navItem}>Contact</Link>
        </nav>
      </div>
    </header>
                    """,
                    "Footer.tsx": """
import React from 'react';
import styles from './Footer.module.css';

export default function Footer() {
  return (
    <footer className={styles.footer}>
      <div className={styles.container}>
        <div className={styles.section}>
          <h2 className={styles.title}>Quick Links</h2>
          <ul className={styles.list}>
            <li><a href="/experiences" className={styles.link}>Experiences</a></li>
            <li><a href="/destinations" className={styles.link}>Destinations</a></li>
            <li><a href="/about" className={styles.link}>About Us</a></li>
            <li><a href="/contact" className={styles.link}>Contact</a></li>
          </ul>
        </div>
        <div className={styles.section}>
          <h2 className={styles.title}>Contact Us</h2>
          <p>Email: info@mgh.com</p>
          <p>Phone: (808) 123-4567</p>
        </div>
        <div className={styles.section}>
          <h2 className={styles.title}>Follow Us</h2>
          <div className={styles.social}>
            <a href="https://www.instagram.com/mgh" className={styles.socialLink}>Instagram</a>
            <a href="https://www.facebook.com/mgh" className={styles.socialLink}>Facebook</a>
          </div>
        </div>
      </div>
      <div className={styles.newsletter}>
        <h2 className={styles.title}>Stay Updated</h2>
        <form className={styles.form}>
          <input type="email" placeholder="Your email address" className={styles.input} />
          <button type="submit" className={styles.button}>Subscribe</button>
        </form>
      </div>
    </footer>
                    """,
                    "Navigation.tsx": "{}"
                },
                "home": {
                    "HeroSection.tsx": """
import React from 'react';
import styles from './HeroSection.module.css';

export default function HeroSection() {
  return (
    <section className={styles.hero}>
      <div className={styles.content}>
        <h1 className={styles.title}>Discover Your Hawaiian Adventure</h1>
        <p className={styles.subtitle}>Experience the beauty of Hawaii like never before.</p>
        <button className={styles.cta}>Book Now</button>
      </div>
    </section>
                    """,
                    "FeaturedExperiences.tsx": "{}",
                    "InteractiveMap.tsx": """
import React, { useEffect, useRef } from 'react';
import mapboxgl from 'mapbox-gl';
import styles from './InteractiveMap.module.css';

mapboxgl.accessToken = 'YOUR_MAPBOX_ACCESS_TOKEN';

export default function InteractiveMap() {
  const mapContainer = useRef(null);
  const map = useRef(null);

  useEffect(() => {
    if (map.current) return;
    map.current = new mapboxgl.Map({
      container: mapContainer.current,
      style: 'mapbox://styles/mapbox/streets-v11',
      center: [-157.858, 21.315],
      zoom: 9
    });

    // Add markers for experiences
    new mapboxgl.Marker()
      .setLngLat([-157.858, 21.315])
      .setPopup(new mapboxgl.Popup().setHTML("<h3>Experience Title</h3><p>Description</p>"))
      .addTo(map.current);
  }, []);

  return <div ref={mapContainer} className={styles.mapContainer} />;
                    """
                },
                "experiences": {
                    "ExperienceCard.tsx": """
import React from 'react';
import { Image, Money } from '@shopify/hydrogen';
import { Product } from '@shopify/hydrogen/storefront-api-types';
import styles from './ExperienceCard.module.css';

interface ExperienceCardProps {
  experience: Product;
}

export default function ExperienceCard({ experience }: ExperienceCardProps) {
  const { title, featuredImage, priceRange } = experience;

  return (
    <div className={styles.card}>
      {featuredImage && (
        <Image
          data={featuredImage}
          className={styles.image}
          width={300}
          height={200}
        />
      )}
      <div className={styles.content}>
        <h3 className={styles.title}>{title}</h3>
        <p className={styles.description}>
          {experience.description?.substring(0, 100)}...
        </p>
        <div className={styles.footer}>
          <Money data={priceRange.minVariantPrice} />
          <button className={styles.button}>Book Now</button>
        </div>
      </div>
    </div>
                    """,
                    "ExperienceList.tsx": "{}",
                    "ExperienceFilters.tsx": "{}"
                },
                "stays": {
                    "StayCard.tsx": "{}",
                    "StayList.tsx": "{}",
                    "StayFilters.tsx": "{}"
                },
                "booking": {
                    "BookingForm.tsx": """
import React from 'react';
import { useForm } from 'react-hook-form';
import styles from './BookingForm.module.css';

interface BookingFormProps {
  onSubmit: (data: any) => void;
}

export default function BookingForm({ onSubmit }: BookingFormProps) {
  const { register, handleSubmit, errors } = useForm();

  return (
    <form onSubmit={handleSubmit(onSubmit)} className={styles.form}>
      <div className={styles.formGroup}>
        <label htmlFor="name" className={styles.label}>
          Name
        </label>
        <input
          id="name"
          name="name"
          ref={register({ required: true })}
          className={styles.input}
        />
        {errors.name && <p className={styles.error}>Name is required</p>}
      </div>
      <div className={styles.formGroup}>
        <label htmlFor="email" className={styles.label}>
          Email
        </label>
        <input
          id="email"
          name="email"
          type="email"
          ref={register({ required: true })}
          className={styles.input}
        />
        {errors.email && <p className={styles.error}>Email is required</p>}
      </div>
      <div className={styles.formGroup}>
        <label htmlFor="date" className={styles.label}>
          Date
        </label>
        <input
          id="date"
          name="date"
          type="date"
          ref={register({ required: true })}
          className={styles.input}
        />
        {errors.date && <p className={styles.error}>Date is required</p>}
      </div>
      <div className={styles.formGroup}>
        <label htmlFor="experience" className={styles.label}>
          Experience
        </label>
        <select
          id="experience"
          name="experience"
          ref={register({ required: true })}
          className={styles.select}
        >
          <option value="">Select an experience</option>
          <option value="hiking">Hiking</option>
          <option value="snorkeling">Snorkeling</option>
        </select>
        {errors.experience && <p className={styles.error}>Experience is required</p>}
      </div>
      <button type="submit" className={styles.button}>
        Book Now
      </button>
    </form>
                    """
                }
            }
        }
    }
}

def create_directory_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_directory_structure(path, content)
        else:
            with open(path, 'w') as file:
                file.write(content)

# Create the directory structure
base_path = os.path.expanduser("~/hy/mgh-website")
os.makedirs(base_path, exist_ok=True)
create_directory_structure(base_path, sitemap)

# Create a ZIP file
zip_file_path = os.path.expanduser("~/hy/mgh-website.zip")
with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(base_path):
        for file in files:
            file_path = os.path.join(root, file)
            zipf.write(file_path, os.path.relpath(file_path, base_path))

print(f"Created ZIP file at {zip_file_path}")
