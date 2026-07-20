import React from 'react';
import {useDoc} from '@docusaurus/plugin-content-docs/client';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

function asList(value) {
  return Array.isArray(value) ? value.filter(Boolean) : value ? [value] : [];
}

function displayDate(value) {
  if (!value) {
    return null;
  }
  if (value instanceof Date) {
    return value.toISOString().slice(0, 10);
  }
  return String(value).slice(0, 10);
}

function PageProfile() {
  const {frontMatter} = useDoc();
  const appliesTo = asList(frontMatter.applies_to);
  const tags = asList(frontMatter.tags);
  const reviewedOn = displayDate(frontMatter.reviewed_on);
  return (
    <aside className={styles.profile} aria-label="Page profile">
      <div><strong>Category:</strong> {frontMatter.category}</div>
      <div><strong>Level:</strong> {frontMatter.difficulty}</div>
      {appliesTo.length > 0 && <div><strong>Applies to:</strong> {appliesTo.join(' · ')}</div>}
      {reviewedOn && <div><strong>Content reviewed:</strong> {reviewedOn}</div>}
      {tags.length > 0 && <div><strong>Topics:</strong> {tags.join(' · ')}</div>}
    </aside>
  );
}

export default function MDXHeading(props) {
  if (props.as !== 'h1') {
    return <Heading {...props} />;
  }
  return <><Heading {...props} /><PageProfile /></>;
}
