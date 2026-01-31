"""
Audio processing utilities
"""
import speech_recognition as sr
from typing import Optional
from app.core.logger import logger


class AudioProcessor:
    """Audio processing utilities"""
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
    
    def transcribe_audio(self, audio_file_path: str) -> Optional[str]:
        """
        Transcribe audio file to text
        
        Args:
            audio_file_path: Path to audio file
            
        Returns:
            Transcribed text or None if failed
        """
        try:
            with sr.AudioFile(audio_file_path) as source:
                audio_data = self.recognizer.record(source)
                text = self.recognizer.recognize_google(audio_data)
                return text
        except sr.UnknownValueError:
            logger.warning("Could not understand audio")
            return None
        except sr.RequestError as e:
            logger.error(f"Could not request results from speech recognition service: {e}")
            return None
        except Exception as e:
            logger.error(f"Error transcribing audio: {e}")
            return None
    
    def transcribe_audio_data(self, audio_data: sr.AudioData) -> Optional[str]:
        """
        Transcribe audio data to text
        
        Args:
            audio_data: Audio data
            
        Returns:
            Transcribed text or None if failed
        """
        try:
            text = self.recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            logger.warning("Could not understand audio")
            return None
        except sr.RequestError as e:
            logger.error(f"Could not request results from speech recognition service: {e}")
            return None
        except Exception as e:
            logger.error(f"Error transcribing audio: {e}")
            return None


# Global audio processor instance
audio_processor = AudioProcessor()
