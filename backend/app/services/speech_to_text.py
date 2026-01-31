"""
Speech to text service
"""
from typing import Optional
from app.utils.audio_utils import audio_processor
from app.core.logger import logger


class SpeechToTextService:
    """Convert speech to text"""
    
    def __init__(self):
        self.audio_processor = audio_processor
    
    def transcribe(self, audio_file_path: str) -> Optional[str]:
        """
        Transcribe audio file to text
        
        Args:
            audio_file_path: Path to audio file
            
        Returns:
            Transcribed text or None
        """
        logger.info(f"Transcribing audio from: {audio_file_path}")
        
        try:
            text = self.audio_processor.transcribe_audio(audio_file_path)
            
            if text:
                logger.info(f"Transcription successful: {len(text)} characters")
            else:
                logger.warning("Transcription returned no text")
            
            return text
        
        except Exception as e:
            logger.error(f"Error in speech to text service: {str(e)}")
            return None


# Global speech to text service instance
speech_to_text_service = SpeechToTextService()
